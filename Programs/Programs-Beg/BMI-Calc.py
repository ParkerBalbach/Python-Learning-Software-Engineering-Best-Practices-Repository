
# Prompt the user to enter their height in feed
height = input("enter your height in ft: ")

# Prompt the user to enter their weight in pounds
weight = input("enter your weight in lbs: ")

# Convert the weight and height inputs from string to floats
num_weight = float(weight)
num_height = float(height)

# Calculate the BMI using the formula: weight (lbs) / (height (ft) ^ 2)
bmi = num_weight / num_height ** 2

# Convert the calculated BMI to an integer
bmi_int = int(bmi)

# Display the calculated BMI to the user
print("your BMI is: ",bmi_int)