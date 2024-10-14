import json

quiz = {
    "What is the capital of Hawaii?": [
        "honolulu",
        "hilo",
        "oahu",
        "ewa beach"
    ],
    "Who is the CEO of Amazon": [
        "jeff bezos",
        "elon musk",
        "bill gates",
        "ronald mcdonald"
    ]
}

quiz_json = json.dumps(quiz)
quiz_file = open('quiz_questions.json', 'w')
quiz_file.write(quiz_json)
quiz_file.close()