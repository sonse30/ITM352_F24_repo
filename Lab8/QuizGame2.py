
quiz = [
    ("What is the capital of Hawaii?", "honolulu"),
    ("Who is the CEO of Amazon?", "jeff bezos")
]

# Loop through the quiz questions
for question, correct_answer in quiz:
    user_answer = input(f"{question}\nYour answer: ")
    
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect.")
