# Prompt the user to input the total bill amount as a floating-point number
bill = float(input("What was the total bill? $"))

# Prompt the user to input the desired percentage for the tip (10%, 12%, or 15%)
tip = int(input("What percentage tip would you like to give? 10, 12, or 15: "))

# Prompt the user to input the number of people who will split the bill
split_bill = int(input("How many people will split the bill? "))

# Calculate the tip percentage as a decimal
tip_percent = tip / 100

# Calculate the total tip by multiplying the bill by the tip percentage
total_tip = bill * tip_percent

# Calculate the total bill by adding the bill amount and the total tip
total_bill = bill + total_tip

# Calculate the amount each person should pay by dividing the total bill by the number of people
bill_per_person = total_bill / split_bill

# Format the bill per person amount with two decimal places
final_amount = "{:.2f}".format(bill_per_person)

# Print the amount that each person should pay
print(f"Each person should pay: ${final_amount}")
