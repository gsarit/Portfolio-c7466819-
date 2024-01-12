# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is usually 24 students, but 
#this is sometimes varied to create groups of similar size. Write a program that
# prompts for the number of students and group size, and then displays how many
# groups will be needed and how many will be left over in a smaller group. 
#How many students? 113 Required group size? 22 There will be 5 groups with 3 students
# left over. For bonus credit, see if you can fix the grammar in the output. 
#So if there were 101 students in groups of 20 the output would be: 
#There will be 5 groups with 1 student left over.
def divide_students():
    # Get user input for the number of students and required group size
    num_students = int(input("How many students? "))
    group_size = int(input("Required group size? "))

    # Calculate the number of groups and the remaining students
    num_groups = num_students // group_size
    remaining_students = num_students % group_size

    # Check the grammar for proper output
    if num_groups == 1:
        group_str = "group"
    else:
        group_str = "groups"

    if remaining_students == 1:
        remaining_str = "student"
    else:
        remaining_str = "students"

    # Display the result
    print(f"There will be {num_groups} {group_str} with {remaining_students} {remaining_str} left over.")

# Call the function
divide_students()