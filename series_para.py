# Ask the user for the number of resistors
total_resistance_series = 0.0
total_resistance_paralell = 0.0
num_resistors = int(input("Enter the number of resistors: "))


# For each resistor
for i in range(num_resistors):
    # Ask the user for the resistance value
    resistance = float(input(f"Enter the resistance of resistor {i+1}: "))
    
    print(f"R_para: {total_resistance_paralell}")
    total_resistance_series += resistance
    print(f"R_series: {total_resistance_series}")


    total_resistance_paralell += (1 / resistance)
    print(f"R_para: {total_resistance_paralell}")

print(f"R_para: {total_resistance_paralell}")    
total_resistance_paralell += (1 / total_resistance_paralell) - total_resistance_paralell

print(f"R_para: {total_resistance_paralell}")

# Print the total resistance
print(f"The total resistance series-resistors is: {total_resistance_series} ohms"  '\n' 
      f"The total resistance paralell-resistors is: {total_resistance_paralell:.5f} ohms")