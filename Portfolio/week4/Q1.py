# Functions are often used to validate input. Write a function that accepts a single
# integer as a parameter and returns True if the integer is in the range 0 to 100 (inclusive),
# or False otherwise. Write a short program to test the function.
def validate_input(integer):
    return 0 <= integer <= 100

# Test the function
user_input = int(input("Enter an integer: "))

if validate_input(user_input):
    print(f"{user_input} is in the range 0 to 100.")
else:
    print(f"{user_input} is outside the range 0 to 100.")