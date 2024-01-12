#Write a program to convert  following tempr
#C to F
#F to C
#C to K
#K to C
#F to K
#K to F
#Your program should show menu first read appropriate output and display the required result

def main():
    print("""'            ..... Menu for Temperature Conversion .....
    
                    1 ...... Celsius to Fahrenheit 
                    2 ...... Celsius to Kelvin 
                    3 ...... Kelvin to Fahrenheit 
                    4 ...... Kelvin to Celsius')
                    5 ...... Fahrenheit to Celsius 
                    6 ...... Fahrenheit to Kelvin """)
    print()
    return input_conversion_choice()


def input_conversion_choice():
    while True:
        try:
            choice = int(input('Enter the number for the conversion: '))
            if choice in [1, 2, 3, 4, 5, 6]:
                return choice
            else:
                print('Enter a valid number between 1 - 6')
        except ValueError:
            print('Enter a valid number between 1 - 6')


def ask_user_temperature(temperature):
    while True:
        try:
            user_input = float(input(f'Enter the temperature in {temperature} : '))
            return user_input
        except ValueError:
            print('Enter valid temperature in decimal.')


# conversion functions
def celsius_to_fahrenheit():
    user_temperature = ask_user_temperature('celsius')
    fahrenheit_temperature = (user_temperature * 9 / 5) + 32
    return str(fahrenheit_temperature) + ' Fahrenheit', user_temperature


def celsius_to_kelvin():
    user_temperature = ask_user_temperature('celsius')
    kelvin_temperature = user_temperature + 273.15
    return str(kelvin_temperature) + ' Kelvin', user_temperature


def kelvin_to_fahrenheit():
    user_temperature = ask_user_temperature('kelvin')
    fahrenheit_temperature = (user_temperature - 273.15) * 9 / 5 + 32
    return str(fahrenheit_temperature) + ' Fahrenheit', user_temperature


def kelvin_to_celsius():
    user_temperature = ask_user_temperature('kelvin')
    celsius_temperature = user_temperature - 273.15
    return str(celsius_temperature) + ' Celsius', user_temperature


def fahrenheit_to_celsius():
    user_temperature = ask_user_temperature('fahrenheit')
    celsius_temperature = (user_temperature - 32) * 5 / 9
    return str(celsius_temperature) + ' Celsius', user_temperature


def fahrenheit_to_kelvin():
    user_temperature = ask_user_temperature('fahrenheit')
    kelvin_temperature = (user_temperature - 32) * 5 / 9 + 273.15
    return str(kelvin_temperature) + ' Kelvin', user_temperature


def print_conversion(converted_temperature, user_temperature, temperature):
    # user_input_temperature = ask_user_temperature('celsius')
    print(f'Conversion : {user_temperature} {temperature} is equal to {converted_temperature}')


# call the functions

user_choice = main()

if user_choice == 1:
    converted_result = celsius_to_fahrenheit()
    print_conversion(converted_result[0], converted_result[1], 'Celsius')

elif user_choice == 2:
    converted_result = celsius_to_kelvin()
    print_conversion(converted_result[0], converted_result[1], 'Celsius')

elif user_choice == 3:
    converted_result = kelvin_to_fahrenheit()
    print_conversion(converted_result[0], converted_result[1], 'Celsius')

elif user_choice == 4:
    converted_result = kelvin_to_celsius()
    print_conversion(converted_result[0], converted_result[1], 'Celsius')

elif user_choice == 5:
    converted_result = fahrenheit_to_celsius()
    print_conversion(converted_result[0], converted_result[1], 'Celsius')

else:
    converted_result = fahrenheit_to_kelvin()
    print_conversion(converted_result[0], converted_result[1], 'Celsius')

    