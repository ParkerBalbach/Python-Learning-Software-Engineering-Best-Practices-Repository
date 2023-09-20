# Prompt the user to input their height in inches and convert it to an integer
height = int(input("What is your height in inches? "))

# Check if the height is greater than or equal to 60 inches (5 feet)
if height >= 60:
    # If the height is 60 inches or more, print "You can ride"
    print("You can ride")
else:
    # If the height is less than 60 inches, print "nope"
    print("Nope")
