question_1 = "What is the capital of Hawaii?"
answer_1 = "honolulu"

question_2 = "Who is the CEO of Amazon?"
answer_2 = "jeff bezos"

user_answer_1 = input(f"{question_1}\nYour answer: ")
if user_answer_1 == answer_1:
    print("Correct!")
else:
    print("Incorrect.")

# Ask second question
user_answer_2 = input(f"{question_2}\nYour answer: ")
if user_answer_2 == answer_2:
    print("Correct!")
else:
    print("Incorrect.")