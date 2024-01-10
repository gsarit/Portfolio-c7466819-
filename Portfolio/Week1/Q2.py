# Make a copy of the previous program, and modify it so that it displays your name. 
#So if your name is Herbert the message should become: Hello, Herbert!
# Note: Very few programs are written from scratch. It is usually best to start 
#with a program that you know works, and ideally does something similar to the new program.

def greet(name):
    message = f"Hello, {name}!"
    print(message)

# Modified program with my name (replace "YourName" with your actual name)
def greet_with_name():
    my_name = "Herbert"  # Replace "Herbert" with your actual name
    greet(my_name)

# Call the modified function
greet_with_name()