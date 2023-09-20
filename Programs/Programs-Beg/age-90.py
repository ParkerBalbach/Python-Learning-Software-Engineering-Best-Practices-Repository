
# Prompt the user for their current age
age = input("What is your current age? ")

# Conver the user's input (which is a string) into an integer
age_int = int(age)

# Calculate the number of years left until the user turns 90
years_left = 90 - age_int

# Calculate the number of days left
days = years_left * 365
# Calculate the number of weeks left
weeks = years_left * 52
# Calculate the number of months left
months = years_left * 12

# Display the results to the user
print(f"You have {days} days, {weeks} weeks, and {months} months left")