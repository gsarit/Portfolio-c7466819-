# Write and test a function that determines if a given integer is a prime number. A
 #prime number is an integer greater than 1 that cannot be produced by multiplying
# two other integers.
def is_prime(n):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be an integer greater than 1.")

    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # If n is divisible by any number in this range, it is not prime
            return False

    # If no factors were found, n is prime
    return True

# Example usage:
number = 17
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")