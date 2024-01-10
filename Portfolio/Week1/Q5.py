# The Head of Computing at the University of Poppleton is tasked with 
#dividing a group of students into lab groups. A lab group is 24 students, 
#since this is the number of PCs in a lab. Write a program that calculates 
#how many groups are needed for the following number of students: 113, 175, 12.
# Display how many full groups there will be, and how many students will be in the smaller "left over" group.

def calculate_lab_groups(num_students, group_size):
    full_groups = num_students // group_size
    remaining_students = num_students % group_size

    return full_groups, remaining_students

def main():
    group_size = 24

    # List of numbers of students
    students_list = [113, 175, 12]

    for num_students in students_list:
        full_groups, remaining_students = calculate_lab_groups(num_students, group_size)
        print(f"For {num_students} students:")
        print(f"Full groups: {full_groups}")
        print(f"Remaining students in the smaller group: {remaining_students}\n")

if __name__ == "__main__":
    main()