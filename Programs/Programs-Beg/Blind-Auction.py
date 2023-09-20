import os
# What is your name:
# What is your bid:
# Other bidders?

# Merge Conflict


# Initialize an empty dictionary to store bids with bidder names as keys and bid amounts as values
bids = {}

"""Determines the winner and highest bidder.

    Args: Dict that contains bidder names as keys and bid amounts as values

    Returns: Winner and amount of $ bid
"""
def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bids:
       bid_amount = bidding_record[bidder]
       # Check if the current bid amount is higher than the current highest bid
       if bid_amount > highest_bid:
           highest_bid = bid_amount
           winner = bidder
           # Format the highest bid amount to display it with two decimal places
           formatted_bid = "{:.2f}".format(highest_bid)
    # Print the winner their highest bid amount
    print(f"The winner is {winner} with a bid of ${formatted_bid}")

# Initialize variable to control the bidding loop
other_bidders = True

# Start loop to allow multiple bidders and their bids
while other_bidders:
    name = input("What is your name: ")
    bid = float(input("What is your bid: $"))
    
    # Add the bidder's name and bid amount to the 'bids' dictionary
    bids[name] = bid

    # Ask the user if there are other bidders or if the bidding is complete
    result = input("If there are other bidders press 'y' otherwise press 'n'\n")
    if result == 'y':
        # Clear the console screen (assumes Windows OS)
        clear = lambda: os.system('cls')
        clear()
    elif result == 'n':
        other_bidders = False

        # Call function to determine and display the winner
        highest_bidder(bids)
        


# final_amount = "{:.2f}".format(bill_per_person)

 
