import json

quiz_file = open('./quiz_questions.json', 'r')
quiz_json = quiz_file.read()
quiz = json.loads(quiz_json)

print(quiz)