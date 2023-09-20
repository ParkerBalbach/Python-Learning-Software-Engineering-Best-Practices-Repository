# Prompt the user to input a two-digit number as a string
user_input = input("Type a two-digit number: ")

# Extract the first digit from the input string
first_digit = user_input[0]

# Extract the second digit from the input string
second_digit = user_input[1]

# Convert the extracted first and second digits back to integers and then add them together
result = int(first_digit) + int(second_digit)

# Print the result of adding the two digits
print(result)
