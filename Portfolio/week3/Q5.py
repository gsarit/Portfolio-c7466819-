# Modify your program a final time so that it executes until the user successfully chooses a password. 
#That is, if the password chosen fails any of the checks, the program should return to asking for the password the first time.

import re

def is_valid_password(password):
    # Check if the password meets the required criteria
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False

    if not re.search("[a-z]", password):
        print("Password must contain at least one lowercase letter.")
        return False

    if not re.search("[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
        return False

    if not re.search("[0-9]", password):
        print("Password must contain at least one digit.")
        return False

    # Password passed all checks
    return True

def get_valid_password():
    while True:
        password = input("Enter your password: ")
        if is_valid_password(password):
            return password
        else:
            print("Please choose a valid password. Try again.")

# Get a valid password from the user
valid_password = get_valid_password()

print("Congratulations! You have successfully chosen a valid password:", valid_password)