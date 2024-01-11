# Modify the "Times Table" again so that the user still enters the number of the table,
# but if this number is negative the table is printed backwards. So entering "-7" would produce the Seven Times 
#Table starting at "12 times" down to "0 times".

def print_times_table(number):
    if number < 0:
        print(f"Printing the {abs(number)} Times Table backwards:")
        for i in range(12, -1, -1):
            result = number * i
            print(f"{number} times {i} is {result}")
    else:
        print(f"Printing the {number} Times Table:")
        for i in range(13):
            result = number * i
            print(f"{number} times {i} is {result}")

# Get user input
user_input = int(input("Enter a number to print its Times Table: "))

# Print the Times Table
print_times_table(user_input)