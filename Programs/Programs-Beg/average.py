
def average_func(lst):
    return sum(lst) / len(lst)

def length_func(lst):
    count = 0
    for i in lst:
        count += 1
    return count




lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = average_func(lst)

print("Average =",average)


def average_loop(lst):
    sum_num = 0
    for num in lst:
        sum_num += num
    
    avg = sum_num / length_func(lst)
    return avg

number = [18,25,3,41,10]
avg = average_loop(number)

print("Average =",avg)


def sum_loop(lst):
    sum_num = 0
    for num in lst:
        sum_num += num
    return sum_num

sumlst = [5,5,5,5,5,5]
sum = sum_loop(sumlst)

print("Sum =", sum)


# new_lst = []

# new_lst = [int(item) for item in input("Enter the list items:").split()]

# print(new_lst)

# new_lst = sum_loop(new_lst)
# print(new_lst)