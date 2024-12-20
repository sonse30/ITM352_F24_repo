from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import random
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

# Load questions from the JSON file that asks from 5 different categories that they all given (Totalling 25 questions)
def load_questions():
    with open('questions.json') as f:
        return json.load(f)

# Load leaderboard data for later use
def load_leaderboard():
    if os.path.exists('leaderboard.json'):
        with open('leaderboard.json') as f:
            return json.load(f)
    return []

# Save leaderboard data that is showcased on the last page and allowing users to compare to others
def save_leaderboard(leaderboard_data):
    with open('leaderboard.json', 'w') as f:
        json.dump(leaderboard_data, f)

#AI Used to Help create indexes for the index.html, leaderboard.html, quiz.html, and result.html
# Route to display the index page (welcome page)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        session['user_name'] = user_name  # Store user name in session
        return redirect(url_for('quiz'))
    return render_template('index.html', user_name=session.get('user_name'))

# Route to start the quiz
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Load and randomize the questions and answer options
    questions = load_questions()
    for category, category_questions in questions.items():
        random.shuffle(category_questions)  # Shuffle question order
        for q in category_questions:
            random.shuffle(q['options'])  # Shuffle answer options

    # Handle form submission
    if request.method == 'POST':
        answers = request.form.to_dict()
        score = 0
        explanations = {}

        # Calculate the score based on the user's answers of incoorect and correct marks
        for category, category_questions in questions.items():
            for question_data in category_questions:
                question_text = question_data['question']
                correct_answer = question_data['correct']
                explanation = question_data['explanation']

                # Get the user's selected answer with bubble filled answers
                user_answer = answers.get(f'question_{question_text}')
                if isinstance(correct_answer, list):  # Multiple correct answers
                    if user_answer and sorted(user_answer.split(',')) == sorted(correct_answer):
                        score += 1
                        explanations[question_text] = explanation
                else:  # Single correct answer only
                    if user_answer == correct_answer:
                        score += 1
                        explanations[question_text] = explanation

        # Store the score in the session which allows for later use on the leaderboard section
        session['score'] = score
        session['total_questions'] = len(answers)
        session['explanations'] = explanations

        # Redirect to result page
        return redirect(url_for('result'))

    return render_template('quiz.html', questions=questions)

# Route to display the result page, which showcases the explanantion for each answer that participants have gotten correct
@app.route('/result', methods=['GET', 'POST'])
def result():
    score = session.get('score', 0)
    total_questions = session.get('total_questions', 0)
    explanations = session.get('explanations', {})
    user_name = session.get('user_name')  # Check for name in session

    if request.method == 'POST':
        # If no user name in session, get it from form
        if not user_name:
            user_name = request.form.get('user_name', 'Anonymous')
            session['user_name'] = user_name

        # Save user score to leaderboard
        leaderboard = load_leaderboard()
        leaderboard.append({'name': user_name, 'score': score})
        leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:10]  # Top 10 only
        save_leaderboard(leaderboard)

        return redirect(url_for('leaderboard'))

    return render_template('result.html', score=score, total_questions=total_questions, explanations=explanations)

# This function loads the leaderboard data from the JSON file.
def load_leaderboard():
    if os.path.exists('leaderboard.json'):
        with open('leaderboard.json') as f:
            return json.load(f)
    return []

# This function saves the updated leaderboard data to the JSON file.
def save_leaderboard(leaderboard_data):
    with open('leaderboard.json', 'w') as f:
        json.dump(leaderboard_data, f)

# This route displays the leaderboard page and showcases who is on the ledaerboard currently
@app.route('/leaderboard')
def leaderboard():
    leaderboard_data = load_leaderboard()  # Load the leaderboard data
    return render_template('leaderboard.html', leaderboard=leaderboard_data)


if __name__ == '__main__':
    app.run(debug=True)
