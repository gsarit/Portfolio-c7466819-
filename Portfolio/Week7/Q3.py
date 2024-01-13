# Write a program that manages a list of countries and their capital cities. 
#It should prompt the user to enter the name of a country. If the program already "knows" the 
#name of the capital city, it should display it. Otherwise it should ask the user to enter it. 
#This should carry on until the user terminates the program (how this happens is up to you).

country_capital_dict = {}

def get_country_input():
    while True:
        country_input = input("Enter the name of a country (or type 'exit' to terminate): ").strip().lower()
        if country_input == 'exit':
            break
        display_or_add_country_capital(country_input)

def display_or_add_country_capital(country):
    if country in country_capital_dict:
        print(f"The capital city of {country.capitalize()} is {country_capital_dict[country]}")
    else:
        capital = input(f"The capital city of {country.capitalize()} is not known. Enter the capital city: ").strip()
        country_capital_dict[country] = capital
        print(f"{country.capitalize()} and its capital {capital} added to the list.")

if __name__ == "__main__":
    print("Welcome to the Country-Capital Management Program!")
    get_country_input()