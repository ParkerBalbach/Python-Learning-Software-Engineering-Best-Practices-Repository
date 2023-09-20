
"""Calculates the average of a list of integers.

    Args: List of numbers

    Returns: Average of numbers in the list
"""
def average_func(lst):
    return sum(lst) / len(lst)


"""Calculates the length of a list.

    Args: List of numbers

    Returns: length of list
"""
def length_func(lst):
    count = 0
    # Iterates through list and counts number of elements
    for i in lst:
        count += 1
    return count



# Predefined list of numbers
lst = [15, 9, 55, 41, 35, 20, 62, 49]

# Calculate the average of the numbers in the list
average = average_func(lst)

# Prints the calculated average
print("Average =",average)

"""Calculates the average of a list of numbers using a loop.

    Args: List of numbers

    Returns: average
"""
def average_loop(lst):
    sum_num = 0
    
    # Iterate through the list and calculates the sum of the numbers
    for num in lst:
        sum_num += num
    
    # Calculate the average by dividing the sum by the length of the list
    avg = sum_num / length_func(lst)
    return avg

# Predefined list of numbers
number = [18,25,3,41,10]

# Calculate the average of the numbers in the list
avg = average_loop(number)

# Print the calculated average
print("Average =",avg)


"""Calculates the sum of a list of numbers using a loop.

    Args: List of numbers

    Returns: sum
"""
def sum_loop(lst):
    sum_num = 0

    # Iterate through the list and calculates the sum of the numbers
    for num in lst:
        sum_num += num
    return sum_num

# Predefined List
sumlst = [5,5,5,5,5,5]

# Calculate the sum of the numbers in the list
sum = sum_loop(sumlst)

# Print Sum
print("Sum =", sum)

