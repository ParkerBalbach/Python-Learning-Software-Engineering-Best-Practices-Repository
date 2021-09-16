# What is your name:
# What is your bid:
# Other bidders?


bids = {}

def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bids:
       bid_amount = bidding_record[bidder]
       if bid_amount > highest_bid:
           highest_bid = bid_amount
           winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


other_bidders = True
while other_bidders:
    name = input("What is your name: ")
    bid = float(input("What is your bid: $"))
    bids[name] = bid

    result = input("If there are other bidders press 'y' otherwise press 'n'\n")
    if result == 'n':
        other_bidders = False
        highest_bidder(bids)

 
