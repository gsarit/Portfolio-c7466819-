# A kindly teacher wishes to distribute a tub of sweets between her pupils. 
#She will first count the sweets and then divide them according to how many pupils attend that day. 
#Write a program that will tell the teacher how many sweets to give to each pupil, and how many she will have left over.
def distribute_sweets(total_sweets, num_pupils):
    sweets_per_pupil = total_sweets // num_pupils
    left_over_sweets = total_sweets % num_pupils

    return sweets_per_pupil, left_over_sweets

# Input from the teacher
total_sweets = int(input("Enter the total number of sweets: "))
num_pupils = int(input("Enter the number of pupils: "))

# Distribute sweets and get the results
sweets_per_pupil, left_over_sweets = distribute_sweets(total_sweets, num_pupils)

# Display the results
print(f"Each pupil will get {sweets_per_pupil} sweets.")
print(f"There will be {left_over_sweets} sweets left over.")