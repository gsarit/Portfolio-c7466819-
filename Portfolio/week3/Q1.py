# Modify your greeting program so that if the user does not enter a name (i.e. they just press enter),
# the program responds "Hello, Stranger!". Otherwise it should print a greeting with their name as before.
# Modified Greeting Program

# Get user input for their name
user_name = input("Enter your name: ")

# Check if the user entered a name or pressed enter
if user_name:
    # If a name is provided, print a greeting with the name
    print("Hello, " + user_name + "!")
else:
    # If no name is provided, print a generic greeting for a stranger
    print("Hello, Stranger!")