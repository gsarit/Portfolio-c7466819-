#write a program to find 10 numbers from user your program should calculate arithmetic mean
#and arithmetic mean for those number
def calculate_arithmetic_mean(numbers):
    total_sum = sum(numbers)
    mean = total_sum / len(numbers)
    return mean

# Input: Get 10 numbers from the user
numbers = []
for i in range(10):
    while True:
        try:
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Calculate arithmetic mean
arithmetic_mean = calculate_arithmetic_mean(numbers)

# Output: Display the results
print(f"\nNumbers: {numbers}")
print(f"Arithmetic Mean: {arithmetic_mean}")
