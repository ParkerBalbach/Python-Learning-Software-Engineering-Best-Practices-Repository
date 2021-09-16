

def highest_num(lst):
    highest_num = 0
    for num in lst:
        if num > highest_num:
            highest_num = num
    return highest_num
        
    


scores = input("Input a list of student scores ").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])

print("highest score is:", highest_num(scores))


