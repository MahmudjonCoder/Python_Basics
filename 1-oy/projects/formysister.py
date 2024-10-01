from termcolor import cprint
import random

QUESTION = "question"
OPTIONS = "options"
ANSWER = "answer"

quiz = [
    {
        QUESTION: "What is the capital of France",
        OPTIONS: ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        ANSWER: "C"
    },
    {
        QUESTION: "What is the capital of Spain",
        OPTIONS: ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        ANSWER: "B"
    },
    {
        QUESTION: "What is the capital of Germany",
        OPTIONS: ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        ANSWER: "A"
    },
    {
        QUESTION: "What is the capital of Italy",
        OPTIONS: ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        ANSWER: "D"
    }
]

random.shuffle(quiz)

score = 0

for index, item in enumerate(quiz, 1):
    print(f"Question {index}: {item[QUESTION]}")
    for option in item[OPTIONS]:
        print(option)
    
    answer = input("Your Answer: ").upper().strip()

    if answer == item[ANSWER]:
        cprint("Correct!\n", "green")
        score += 1
    else:
        cprint(f"Wrong! The correct answer is {item[ANSWER]} \n", "red")

print(f"Quiz over! your final score is {score}")