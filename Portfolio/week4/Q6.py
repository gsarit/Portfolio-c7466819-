# Write a program that takes a centigrade temperature and displays the equivalent in fahrenheit.
# The input should be a number followed by a letter C. The output should be in the same format.
def celsius_to_fahrenheit(input_str):
    try:
        # Extracting the numerical value from the input string
        celsius = float(input_str[:-1])
        
        # Converting Celsius to Fahrenheit
        fahrenheit = (celsius * 9/5) + 32
        
        # Displaying the result in the same format
        print(f"{fahrenheit:.2f}F")
    except ValueError:
        print("Invalid input. Please enter a valid temperature followed by 'C'.")

# Get input from the user
temperature_input = input("Enter temperature in centigrade (e.g., 25C): ")

# Convert and display the result
celsius_to_fahrenheit(temperature_input)