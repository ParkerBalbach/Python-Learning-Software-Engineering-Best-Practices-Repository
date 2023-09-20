"""Takes two arguments and prints a greeting.

    Args:
        name: name
        name2: name2

    Returns: Printed Greetings for the two args
"""
def greet(name, name2):
    # Print a greeting using the 'name' argument
    print(f"Hello {name}")
    
    # Print a follow-up greeting using the 'name2' argument
    print(f"How do you do {name2}")

# Prompt the user to input their name
name = input("Please enter your name: ")

# Prompt the user to input their mother's name
name2 = input("Please enter your mother's name: ")

# Call the 'greet' function with the user's name and their mother's name as arguments
greet(name, name2)
