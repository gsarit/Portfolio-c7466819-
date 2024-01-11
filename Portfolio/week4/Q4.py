# When processing data it is often useful to remove the last character from some input 
#(it is often a newline). Write and test a function that takes a string parameter and returns
# it with the last character removed. (If the string contains one or fewer characters, return it unchanged.)
def remove_last_character(input_string):
    if len(input_string) <= 1:
        return input_string
    else:
        return input_string[:-1]

# Test the function
test_string1 = "Hello, world!\n"
test_string2 = "A"
test_string3 = ""

result1 = remove_last_character(test_string1)
result2 = remove_last_character(test_string2)
result3 = remove_last_character(test_string3)

print("Original String 1:", repr(test_string1))
print("Result 1:", repr(result1))

print("Original String 2:", repr(test_string2))
print("Result 2:", repr(result2))

print("Original String 3:", repr(test_string3))
print("Result 3:", repr(result3))