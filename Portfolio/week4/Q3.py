# Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user 
#entered their name differently. So if the user entered arthur, ARTHUR, or even arTHur the name should be displayed as Arthur.
def greet_user():
    # Get user input for the name
    user_input = input("Enter your name: ")

    # Capitalize the first letter and convert the rest to lowercase
    formatted_name = user_input.capitalize()

    # Greet the user with the formatted name
    print(f"Hello, {formatted_name}!")

# Call the greet_user function
greet_user()