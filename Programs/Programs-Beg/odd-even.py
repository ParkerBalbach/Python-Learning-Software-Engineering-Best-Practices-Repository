# Prompt the user to input a number and convert it to an integer
user_input = int(input("Please enter a number: "))

# Check if the user's input is divisible by 2 (i.e., even)
if user_input % 2 == 0:
    # If the remainder of the division by 2 is 0, the number is even
    print("Your number is even.")
else:
    # If the remainder is not 0, the number is odd
    print("Your number is odd.")
