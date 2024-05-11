def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for question_info in questions:
        question, options, correct_answer = question_info
        print(question)
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        user_answer = input("Your answer (enter the number): ")
        if user_answer.isdigit() and int(user_answer) - 1 == correct_answer:
            print("Correct!")
            score += 1
        else:
            correct_option_text = options[correct_answer]
            print(f"Incorrect! The correct answer is: {correct_option_text}")
        print()  # Print a blank line for better separation between questions

    print("Quiz completed!")
    print(f"Your final score is {score}/{total_questions}")

# Define your quiz questions and answers
quiz_questions = [
    ("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], 2),
    ("Which planet is known as the Red Planet?", ["Jupiter", "Mars", "Saturn", "Venus"], 1),
    ("Who wrote 'Hamlet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], 1),
    ("What is the chemical symbol for water?", ["CO2", "O2", "H2O", "NaCl"], 2),
    ("What is the largest organ in the human body?", ["Heart", "Skin", "Liver", "Kidney"], 1),
    ("In which continent is the Amazon Rainforest located?", ["Africa", "North America", "Asia", "South America"], 3),
    ("What year did the Titanic sink?", ["1905", "1912", "1923", "1898"], 1),
    ("Who painted the Mona Lisa?", ["Vincent Van Gogh", "Pablo Picasso", "Claude Monet", "Leonardo da Vinci"], 3),
    ("What is the hardest natural substance on Earth?", ["Gold", "Iron", "Diamond", "Platinum"], 2),
    ("Who is known as the father of modern physics?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"], 2)
]

# Run the quiz
run_quiz(quiz_questions),
