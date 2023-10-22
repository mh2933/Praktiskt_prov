# Ask the user for the number of resistors
num_resistors = int(input("Enter the number of resistors: "))

# Ask the user for the type of connection
connection = input("Type 's' for series connection, or 'p' for parallel connection: ")

# Initialize total resistance to 0 for series, and to 1 for parallel
if connection.lower() == 's':
    total_resistance = 0.0
elif connection.lower() == 'p':
    total_resistance = 0.0

# For each resistor
for i in range(num_resistors):
    # Ask the user for the resistance value
    resistance = float(input(f"Enter the resistance of resistor {i+1}: "))

    # Add the resistance value to the total resistance
    if connection.lower() == 's':
        total_resistance += resistance
    elif connection.lower() == 'p':
        total_resistance += 1 / resistance

# If the connection is parallel, take the reciprocal of the total resistance
if connection.lower() == 'p':
    total_resistance = 1 / total_resistance

# Print the total resistance
print(f"The total resistance of the {connection} resistors is: {total_resistance} ohms")