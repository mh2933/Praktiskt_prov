# Ask the user to enter the resistor values
resistor_values = input("Enter the resistor values separated by a space: ")

# Convert the input string into a list of floats
resistors = [float(value) for value in resistor_values.split()]

# Calculate the total series resistance
total_resistance_series = sum(resistors)

# Calculate the total parallel resistance
total_resistance_paralell = 1 / sum(1 / resistance for resistance in resistors)

# Print the total resistance
print(f"The total resistance series-resistors is: {total_resistance_series:.2f} ohms"  '\n' 
      f"The total resistance paralell-resistors is: {total_resistance_paralell:.5f} ohms")l