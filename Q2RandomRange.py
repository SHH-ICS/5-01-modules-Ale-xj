import random


lower_bound = int(input("Enter the lower bound of the range: "))
upper_bound = int(input("Enter the upper bound of the range: "))


random_number = random.randint(lower_bound, upper_bound)

# Display the result
print(f"A random number between {lower_bound} and {upper_bound} is: {random_number}")
