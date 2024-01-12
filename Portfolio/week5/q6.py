#write a program to read marks for 5 subject of a student.Your program should give the average result using
#lambda expression.
# Input: Get marks for 5 subjects from the user
marks = []
for i in range(5):
    while True:
        try:
            mark = float(input(f"Enter mark for subject {i + 1}: "))
            marks.append(mark)
            break
        except ValueError:
            print("Invalid input. Please enter a valid mark.")

# Lambda expression to calculate average
calculate_average = lambda marks: sum(marks) / len(marks)

# Calculate and display the average result
average_result = calculate_average(marks)
print(f"\nMarks: {marks}")
print(f"Average Result: {average_result}")