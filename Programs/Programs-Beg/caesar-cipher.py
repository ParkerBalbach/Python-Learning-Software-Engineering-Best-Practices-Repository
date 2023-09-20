

# List of letters in english alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


"""Performs the Casesar cipher encript/decript.

    Args: 
        direction: encode or decode
        text: Text
        shift: Range from (0-25)

    Returns: encoded or decoded cipher
"""
def caesar(direction, text, shift):
    end_text = ""
    
    # If the direction is 'decode' reverse the shift to decrypt
    if direction == "decode":
        shift *= -1

    # Iterate through each character in the input text    
    for char in text:
        if char in alphabet:
            # Find the position of the character in the alphabet
            position = alphabet.index(char)
            # Calculate the new position by adding the shift
            new_position = position + shift
            # Append the character at the new position
            end_text += alphabet[new_position]
        else:
            # If the character is not used then keep it unchanged
            end_text += char
    
    # Print the result and indicate if encode or decode
    print(f"Here's the {direction}d result: {end_text}")

# Initialize a variable to control loop
should_continue = True

# Start a loop to allow the user to perform multiple encripts and decrypts
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Ensure that the shift value is between 0-25
    shift = shift % 26
    # Call the function to perform encrypt/decrypt
    caesar(direction, text, shift)

    # Ask the user if they want to continue or quit
    result = input("Type 'y' if you want to go again. Type 'n' to quit.\n")
    if result == 'n':
        print("Goodbye!")
        should_continue = False



