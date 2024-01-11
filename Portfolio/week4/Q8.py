# Modify the previous program so that it can process any number of values. 
#The input terminates when the user just pressed "Enter" at the prompt rather than entering a value.
# Program to process any number of values until the user presses "Enter"
def calculate_average():
    numbers = []
    
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        
        if user_input == "":
            break  # Exit the loop if the user presses Enter without entering a value
        else:
            try:
                number = float(user_input)
                numbers.append(number)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    if not numbers:
        print("No numbers entered.")
    else:
        average = sum(numbers) / len(numbers)
        print("Average:", average)

if __name__ == "__main__":
    calculate_average()