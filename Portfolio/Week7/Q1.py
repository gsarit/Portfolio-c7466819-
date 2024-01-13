# Write and test a function that takes a string as a parameter and returns a sorted list of all 
#the unique letters used in the string. So, if the string is cheese, the list returned should be ['c', 'e', 'h', 's'].
def unique_letters_sorted(input_string):
    # Convert the string to lowercase to make the comparison case-insensitive
    input_string = input_string.lower()
    
    # Use set to get unique letters and then convert it to a sorted list
    unique_letters = sorted(set(char for char in input_string if char.isalpha()))
    
    return unique_letters

# Test the function with the example "cheese"
input_str = "cheese"
result = unique_letters_sorted(input_str)
print(result)