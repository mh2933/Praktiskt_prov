# #resistor_value = []

# resistor_value = input('Ange resistorer: ')
# #int[resistor_value] = resistor_value

# resistor_value = float(resistor_value)
# resistor_list = []

# for num in resistor_value:
#     resistor_list.append(resistor_value)


# #print(accumulator)
# #print(resistor_list)    
# #print(resistor_value)

# print(f'resistor_value: {resistor_value}')
# print(type(resistor_value))

# print(f'resistor_value: {resistor_list}')
# print(type(resistor_list))


# Ask the user to enter the resistor values
resistor_values = input('Ange resistorer: ')

# Split the input into a list of strings
resistor_values = resistor_values.split()

# Convert each string in the list to a float and store them in a new list
resistor_list = [float(value) for value in resistor_values]

# Print the list of resistor values and its type
print(f'resistor_value: {resistor_list}')
print(type(resistor_list))