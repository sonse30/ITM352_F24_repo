# Import the quiz data and correct answers from the external file
from quiz_data import quiz_data, correct_answers, explanations

def quiz():
    score = 0  # To track the user's score
    total_questions = len(quiz_data)

    # Loop through each question and ask the user
    for question, options in quiz_data.items():
        print("\n" + question)  # Print the question

        # Print the options with labels 'a', 'b', 'c', 'd'
        for idx, option in enumerate(options, 97):  # 97 is the ASCII value for 'a'
            print(f"{chr(idx)}) {option}")

        # Keep prompting until the user provides a valid answer (a-d)
        while True:
            answer = input("Your answer (a/b/c/d): ").lower()
            if answer in ['a', 'b', 'c', 'd']:  # Validate the input
                break
            else:
                print("Invalid input. Please enter 'a', 'b', 'c', or 'd'.")

        # Check if the answer is correct
        if answer in correct_answers[question]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

        print(f"Explanation: {explanations[question]}")

    # Display the final score
    print(f"\nQuiz finished! Your final score is {score}/{total_questions}.")

# Run the quiz
if __name__ == "__main__":
    quiz()
