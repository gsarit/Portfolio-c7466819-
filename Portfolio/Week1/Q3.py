# Over the summer, temperatures in Yorkshire reached 38.4C. Write a program 
#that converts this value in Celsius to the equivalent temperature in Fahrenheit, and then displays both.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Temperature in Celsius
celsius_temperature = 38.4

# Convert Celsius to Fahrenheit
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

# Display the results
print(f'Temperature in Celsius: {celsius_temperature}°C')
print(f'Temperature in Fahrenheit: {fahrenheit_temperature}°F')