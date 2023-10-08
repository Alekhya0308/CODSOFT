import random

# Define a list of questions with options and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B) Paris"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "answer": "Carbon dioxide"
    },
    {
        "question": "What is 7 multiplied by 8?",
        "answer": "56"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A) Elephant", "B) Giraffe", "C) Blue Whale", "D) Lion"],
        "answer": "C) Blue Whale"
    }
]

def welcome_message():
    print("Welcome to the Quiz Game!")
    print("Rules:")
    print("1. Answer multiple-choice questions by entering the letter (A, B, C, or D) corresponding to your choice.")
    print("2. For fill-in-the-blank questions, type your answer as text.")
    print("3. Let's get started!\n")

def ask_question(question_data):
    print(question_data["question"])
    if "options" in question_data:
        for option in question_data["options"]:
            print(option)
    user_answer = input("Your answer: ").strip().capitalize()
    return user_answer

def evaluate_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer is: {correct_answer}")
        return False

def play_quiz(quiz_data):
    score = 0
    for question_data in quiz_data:
        user_answer = ask_question(question_data)
        if "options" in question_data:
            is_correct = evaluate_answer(user_answer, question_data["answer"])
        else:  # Fill-in-the-blank question
            is_correct = evaluate_answer(user_answer, question_data["answer"].lower())
        if is_correct:
            score += 1
        print("\n" + "-" * 30)
    
    return score

def main():
    welcome_message()
    play_again = True
    while play_again:
        score = play_quiz(quiz_data)
        total_questions = len(quiz_data)
        print(f"\nQuiz completed! Your score: {score}/{total_questions}")
        if score == total_questions:
            print("Congratulations! You got all the questions right!")
        play_again = input("Do you want to play again? (yes/no): ").strip().lower() == "yes"

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
