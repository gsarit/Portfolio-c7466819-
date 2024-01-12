#write a program to read marks for 5 subject of a student.Your program should give the average result using
#lambda expression.


calculate_average = lambda marks: sum(marks) / len(marks)

marks = []
for i in range(5):
    subject_mark = float(input(f"Enter marks for the subject {i+1}: "))
    marks.append(subject_mark)


average = calculate_average(marks)
print("The average marks are:", average)


