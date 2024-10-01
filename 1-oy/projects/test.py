# from termcolor import cprint
# import random

# QUESTION = "question"
# OPTIONS = "options"
# ANSWER = "answer"

# quiz = [
#     {
#         QUESTION: "10+23",
#         OPTIONS: ["A. 23", "B. 33", "C. 234", "D. 12345"],
#         ANSWER: "B"
#     },
#     {
#         QUESTION: "5+10",
#         OPTIONS: ["A. 15", "B. 21", "C. 1", "D. 4"],
#         ANSWER: "B"
#     },
#     {
#         QUESTION: "8+4",
#         OPTIONS: ["A. 23", "B. 12", "C. 56", "D. 12"],
#         ANSWER: "D"
#     },
#     {
#         QUESTION: "2+3",
#         OPTIONS: ["A. 6", "B. 4", "C. 2", "D. 5"],
#         ANSWER: "D"
#     },
#     {    
#         QUESTION: "2+1",
#         OPTIONS: ["A. 6", "B. 1", "C. 3", "D. 0"],
#         ANSWER: "C"
#     },
#     {
#         QUESTION: "10-4",
#         OPTIONS: ["A. 11", "B. 6", "C. 14", "D. 90"],
#         ANSWER: "B"
#     },
#     {
#         QUESTION: "20-10",
#         OPTIONS: ["A. 10", "B. 3", "C. 234", "D. 54"],
#         ANSWER: "A"
#     },
#     {
#         QUESTION: "20+1",
#         OPTIONS: ["A. 22", "B. 21", "C. 23", "D. 24"],
#         ANSWER: "B"
#     },
#     {
#         QUESTION: "15-5",
#         OPTIONS: ["A. 23", "B. 13", "C. 10", "D. 9"],
#         ANSWER: "C"
#     },
#     {
#         QUESTION: "12+6",
#         OPTIONS: ["A. 0", "B. 10", "C. 16", "D. 18"],
#         ANSWER: "D"
#     }
# ]

# random.shuffle(quiz)

# score = 0

# for index, item in enumerate(quiz, 1):
#     print(f"Question {index}: {item[QUESTION]}")
#     for option in item[OPTIONS]:
#         print(option)
    
#     answer = input("Your Answer: ").upper().strip()

#     if answer == item[ANSWER]:
#         cprint("Correct!\n", "green")
#         score += 1
#     else:
#         cprint(f"Wrong! The correct answer is {item[ANSWER]} \n", "red")

# print(f"Quiz over! your final score is {score}")




