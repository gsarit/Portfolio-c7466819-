# Write a program that reads 6 temperatures (in the same format as before), 
#and displays the maximum, minimum, and mean of the values. Hint: You should know there
# are built-in functions for max and min. If you hunt, you might also find one for the mean.
def main():
    temperatures = []

    # Read 6 temperatures
    for i in range(6):
        temperature = float(input(f"Enter temperature {i + 1}: "))
        temperatures.append(temperature)

    # Calculate maximum, minimum, and mean
    max_temperature = max(temperatures)
    min_temperature = min(temperatures)
    mean_temperature = sum(temperatures) / len(temperatures)

    # Display the results
    print(f"\nMaximum Temperature: {max_temperature}")
    print(f"Minimum Temperature: {min_temperature}")
    print(f"Mean Temperature: {mean_temperature}")

if __name__ == "__main__":
    main()