# Quiz App in
questions = {
    1: {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    2: {
        "question": "Who is the president of the United States?",
        "answer": "Joe Biden"
    },
    3: {
        "question": "What is the capital of England?",
        "answer": "London"
    }
}

def display_question(question):
    print(f"{question['question']}")

def get_user_answer():
    user_answer = input("Your answer: ")
    return user_answer

def check_answer(question, user_answer):
    if user_answer.lower() == question["answer"].lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {question['answer']}")

def main():
    for question_id, question in questions.items():
        display_question(question)
        user_answer = get_user_answer()
        check_answer(question, user_answer)

if __name__ == "__main__":
    main()
