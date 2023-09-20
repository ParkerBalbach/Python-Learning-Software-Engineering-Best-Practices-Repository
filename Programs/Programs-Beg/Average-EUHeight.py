
"""Calculates the average of a list of heights.

    Args: List that contains heights

    Returns: Prints the rounded averages
"""
def height_calc(lst):
    sum = 0
    
    # Iterate through the list of heights and calculate the sum
    for height in lst:
        sum += height
    
    # Calculate the average by dividing the sum by the number of elements in the list
    avg = sum / len(lst)

    # Print the rounded average value
    return print(round(avg))
    
# Defined list of student heights
student_height = [180, 124, 165, 173, 189, 169, 146]

# Calls height_calc function and uses the predefined list
height_calc(student_height)

# Prompts the user to input a list of student heights as a string and splits them into individual values
heights = input("Input a list of student heights ").split()

# Iterates through split user input and changes the strings into integers
for n in range(0, len(heights)):
    heights[n] = int(heights[n])

# Calls height_calc function and used user inputed list
height_calc(heights)


"""Calculates the length of a list.

    Args: List

    Returns: Prints the length of user-inputted list
"""
def length(lst):
    length = 0

    # Iterates through the list and counts the number of elements
    for len in lst:
        length += 1
    return length

# Prompts the user to input a list of student heights as a string and splits into individual values
new_lst = input("Input a list of student heights ").split()

# Calculate and print the length of user-inputted list
new_length = length(new_lst)
print(new_length)

