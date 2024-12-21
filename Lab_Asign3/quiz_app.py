from flask import Flask, render_template, request, redirect, url_for, session
import json
import random
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management


# Load questions from the JSON file
def load_questions():
    try:
        with open('Lab_Asign3/questions.json', 'r') as f:
            data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("Invalid questions format: Root element must be a dictionary.")
            return data
    except FileNotFoundError:
        print("Error: 'questions.json' file not found.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {}
    except ValueError as e:
        print(f"Error: {e}")
        return {}


# Load leaderboard data
def load_leaderboard():
    if os.path.exists('leaderboard.json'):
        with open('leaderboard.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


# Save leaderboard data
def save_leaderboard(leaderboard_data):
    with open('leaderboard.json', 'w', encoding='utf-8') as f:
        json.dump(leaderboard_data, f, indent=4)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        session['user_name'] = user_name  # Store user name in session
        return redirect(url_for('quiz'))
    return render_template('index.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions = load_questions()

    #if not questions:
     #   return "Error loading questions. Please check 'questions.json'."

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

                user_answer = answers.get(f'question_{question_text}')
                if isinstance(correct_answer, list):  # Multiple correct answers
                    user_answers = user_answer.split(',') if user_answer else []
                    if sorted(user_answers) == sorted(correct_answer):
                        score += 1
                        explanations[question_text] = explanation
                else:  # Single correct answer
                    if user_answer == correct_answer:
                        score += 1
                        explanations[question_text] = explanation

        # Store results in session
        session['score'] = score
        session['total_questions'] = sum(len(q) for q in questions.values())
        session['explanations'] = explanations

        return redirect(url_for('result'))

    return render_template('quiz.html', questions=questions)


@app.route('/result', methods=['GET', 'POST'])
def result():
    score = session.get('score', 0)
    total_questions = session.get('total_questions', 0)
    explanations = session.get('explanations', {})
    user_name = session.get('user_name')

    if request.method == 'POST':
        if not user_name:
            user_name = request.form.get('user_name', 'Anonymous')
            session['user_name'] = user_name

        leaderboard = load_leaderboard()
        leaderboard.append({'name': user_name, 'score': score})
        leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:10]
        save_leaderboard(leaderboard)

        return redirect(url_for('leaderboard'))

    return render_template('result.html', score=score, total_questions=total_questions, explanations=explanations)


@app.route('/leaderboard')
def leaderboard():
    leaderboard_data = load_leaderboard()
    return render_template('leaderboard.html', leaderboard=leaderboard_data)


if __name__ == '__main__':
    app.run(debug=True)
