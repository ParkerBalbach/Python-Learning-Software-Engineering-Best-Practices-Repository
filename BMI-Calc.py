

height = input("enter your height in ft: ")
weight = input("enter your weight in lbs: ")

num_weight = float(weight)
num_height = float(height)

bmi = num_weight / num_height ** 2
bmi_int = int(bmi)

print("your BMI is: ",bmi_int)