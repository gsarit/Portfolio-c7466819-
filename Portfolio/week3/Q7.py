# Modify your "Times Table" program so that the user enters the number of the table they require.
# This number should be between 0 and 12 inclusive.
def print_times_table(table_number):
    if 0 <= table_number <= 12:
        print(f"Times Table for {table_number}:")
        for i in range(1, 11):
            result = table_number * i
            print(f"{table_number} x {i} = {result}")
    else:
        print("Please enter a number between 0 and 12 inclusive.")

# Get user input
user_input = input("Enter the number for the times table (0 to 12): ")

# Check if the input is a valid integer
if user_input.isdigit():
    table_number = int(user_input)
    print_times_table(table_number)
else:
    print("Please enter a valid integer.")