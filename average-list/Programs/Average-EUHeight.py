
def height_calc(lst):
    sum = 0
    for height in lst:
        sum += height
    
    avg = sum / len(lst)
    return print(round(avg))
    



student_height = [180, 124, 165, 173, 189, 169, 146]

height_calc(student_height)


heights = input("Input a list of student heights ").split()
for n in range(0, len(heights)):
    heights[n] = int(heights[n])

height_calc(heights)


def length(lst):
    length = 0
    for len in lst:
        length += 1
    return length


new_lst = input("Input a list of student heights ").split()
new_length = length(new_lst)
print(new_length)

