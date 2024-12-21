from flask import Flask, render_template, request, redirect, url_for, session
import json
import random
import os
from datetime import timedelta

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')  # Use an environment variable for security
app.permanent_session_lifetime = timedelta(hours=1)  # Set session expiry

# Load questions from the JSON file
def load_questions():
    try:
        with open('questions.json') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Load leaderboard data
def load_leaderboard():
    if os.path.exists('leaderboard.json'):
        try:
            with open('leaderboard.json') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

# Save leaderboard data
def save_leaderboard(leaderboard_data):
    try:
        with open('leaderboard.json', 'w') as f:
            json.dump(leaderboard_data, f)
    except Exception as e:
        print(f"Error saving leaderboard: {e}")

# Route to display the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        if user_name:
            session['user_name'] = user_name  # Store user name in session
            return redirect(url_for('quiz'))
    return render_template('index.html', user_name=session.get('user_name'))

# Route to start the quiz
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions = load_questions()
    if not questions:
        return "Questions not found. Please ensure 'questions.json' is correctly formatted."

    # Shuffle questions and options
    for category, category_questions in questions.items():
        random.shuffle(category_questions)
        for q in category_questions:
            random.shuffle(q['options'])

    if request.method == 'POST':
        answers = request.form.to_dict()
        score = 0
        explanations = {}

        # Calculate the score
        for category, category_questions in questions.items():
            for question_data in category_questions:
                question_text = question_data['question']
                correct_answer = question_data['correct']
                explanation = question_data['explanation']

                # User's selected answer
                user_answer = answers.get(f'question_{question_text}')
                if isinstance(correct_answer, list):  # Multiple correct answers
                    if user_answer and sorted(user_answer.split(',')) == sorted(correct_answer):
                        score += 1
                        explanations[question_text] = explanation
                else:  # Single correct answer
                    if user_answer == correct_answer:
                        score += 1
                        explanations[question_text] = explanation

        # Store score and explanations in session
        session['score'] = score
        session['total_questions'] = sum(len(qs) for qs in questions.values())
        session['explanations'] = explanations

        return redirect(url_for('result'))

    return render_template('quiz.html', questions=questions)

# Route to display the result page
@app.route('/result', methods=['GET', 'POST'])
def result():
    score = session.get('score', 0)
    total_questions = session.get('total_questions', 0)
    explanations = session.get('explanations', {})
    user_name = session.get('user_name', 'Anonymous')

    if request.method == 'POST':
        # Save user score to leaderboard
        leaderboard = load_leaderboard()
        leaderboard.append({'name': user_name, 'score': score})
        leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:10]  # Top 10 only
        save_leaderboard(leaderboard)

        return redirect(url_for('leaderboard'))

    return render_template('result.html', score=score, total_questions=total_questions, explanations=explanations)

# Route to display the leaderboard page
@app.route('/leaderboard')
def leaderboard():
    leaderboard_data = load_leaderboard()
    return render_template('leaderboard.html', leaderboard=leaderboard_data)

if __name__ == '__main__':
    app.run(debug=True)
