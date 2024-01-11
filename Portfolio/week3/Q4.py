# Modify your program again so that the chosen password cannot be one of a list of common passwords, 
#defined thus: BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

def get_password():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Password is too short. It must be at least 8 characters long.")
        elif password in BAD_PASSWORDS:
            print("Common password! Please choose a different one.")
        else:
            return password

# Example usage
chosen_password = get_password()
print("Chosen password:", chosen_password)