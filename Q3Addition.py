import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

print(f"What is {num1} + {num2}?")

user_answer = int(input("Your answer: "))


correct_answer = num1 + num2


if user_answer == correct_answer:
    print("Correct! Well done.")
else:
    print(f"Oops! The correct answer is {correct_answer}.")
