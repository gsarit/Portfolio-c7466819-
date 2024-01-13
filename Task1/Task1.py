def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive integer!")
            else:
                return value
        except ValueError:
            print("Plea2se enter a number!")

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response == 'y' or response == 'n':
            return response
        else:
            print('Please answer "Y" or "N".')

print("BPP Pizza Price Calculator")
print("==========================")

num_pizzas = get_int_input("How many pizzas ordered? ")

delivery_required = get_yes_no_input("Is delivery required? ")

is_tuesday = get_yes_no_input("Is it Tuesday? ")

used_app = get_yes_no_input("Did the customer use the app? ")

# Calculating the total price based on inputs
base_price_per_pizza = 10  # Assuming base price of a pizza is $10

total_price = num_pizzas * base_price_per_pizza

if delivery_required == 'y':
    total_price += 5  # Additional $5 for delivery

if is_tuesday == 'y':
    total_price -= 2  # $2 discount on Tuesdays

if used_app == 'y':
    total_price *= 0.9  # 10% discount for app users

print(f"The total price for {num_pizzas} pizzas is ${total_price:.2f}")