# Loop through numbers from 1 to 100 (inclusive)
for number in range(1, 101):
    # Check if the number is divisible by both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")  # If divisible by both 3 and 5, print "FizzBuzz"
    
    # Check if the number is divisible by 5
    elif number % 5 == 0:
        print("Buzz")  # If divisible by 5, print "Buzz"
    
    # Check if the number is divisible by 3
    elif number % 3 == 0:
        print("Fizz")  # If divisible by 3, print "Fizz"

    # If none of the above conditions are met, print the number itself
    else:
        print(number)
