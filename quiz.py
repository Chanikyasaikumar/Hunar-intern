def quiz_app():
    # Define the questions and answers
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Berlin", "B. Madrid", "C. Delhi", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "What is 2 * 7?",
            "options": ["A. 3", "B. 21", "C. 5", "D. 6"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
            "answer": "A"
        }
    ]

    score = 0

    # Loop through each question
    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")
        for option in question["options"]:
            print(option)
        answer = input("Your answer (A, B, C, or D): ").strip().upper()

        # Check the answer
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question['answer']}.\n")

    # Print the final score
    print(f"Your final score is {score} out of {len(questions)}.")

# Run the quiz application
if __name__ == "__main__":
    quiz_app()
