
def average_func(lst):
    return sum(lst) / len(lst)


lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = average_func(lst)

print("Average =",average)


def average_loop(lst):
    sum_num = 0
    for num in lst:
        sum_num = sum_num + num
    
    avg = sum_num / len(lst)
    return avg

number = [18,25,3,41,5]
avg = average_loop(number)

print("Average =",avg)


def sum_loop(lst):
    sum_num = 0
    for num in lst:
        sum_num = sum_num + num
    return sum_num

sumlst = [5,5,5,5,5,5]
sum = sum_loop(sumlst)

print("Sum =", sum)


