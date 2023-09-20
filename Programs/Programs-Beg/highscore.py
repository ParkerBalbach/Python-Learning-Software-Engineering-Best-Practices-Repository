"""Find the highest number in a list.

    Args: List of numbers

    Returns: highest number in the list
"""
def highest_num(lst):
    highest_num = 0
    
    # Iterate through the list of numbers
    for num in lst:
        # Compare the current number to the current highest number
        if num > highest_num:
            highest_num = num
    
    # Return the highest number found
    return highest_num

# Prompt the user to input a list of student scores as a string and split it into individual values
scores = input("Input a list of student scores ").split()

# Convert the input values from strings to integers
for n in range(0, len(scores)):
    scores[n] = int(scores[n])

# Call function to find the highest score in the list and print it
print("The highest score is:", highest_num(scores))
