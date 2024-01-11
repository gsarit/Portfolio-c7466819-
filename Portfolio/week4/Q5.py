# Write and test a function that converts a temperature measured in degrees 
#centigrade into the equivalent in fahrenheit, and another that does the reverse conversion. 
#Test both functions. (Google will find you the formulae).
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    Formula: F = (9/5)C + 32
    """
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    Formula: C = (5/9)(F - 32)
    """
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

# Test the functions
celsius_temperature = 25
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature:.2f} degrees Fahrenheit.")

fahrenheit_temperature = 77
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_temperature:.2f} degrees Celsius.")