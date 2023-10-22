resistor_values = input("Enter the resistor values separated by a space: ")

# Split the input into list of strings
resistor_values = resistor_values.split()

# Initialize total resistances to 0
total_resistance_series = 0.0
total_resistance_paralell = 0.0

# For each resistor
for value in resistor_values:
    # Convert the string to a float
    resistance = float(value)
    
    # Add the resistance value to the total series resistance
    total_resistance_series += resistance

    # Add the reciprocal of the resistance value to the total parallel resistance
    total_resistance_paralell += 1 / resistance

total_resistance_paralell = 1 / total_resistance_paralell

# Print the total resistance
print(f"The total resistance series-resistors is: {total_resistance_series} ohms"  '\n' 
      f"The total resistance paralell-resistors is: {total_resistance_paralell:.5f} ohms")