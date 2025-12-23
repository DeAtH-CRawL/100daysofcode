import hammer_art 
import os
print(hammer_art.logo)
item_name = input("What is the item you are bidding on? ")
name = input("What is your name? ")
bid = float(input("What is your bid? $"))


bids = {
    name: bid
}
should_continue = True
while should_continue:
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "yes":
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        print(hammer_art.logo)
        print(f"Bidding on: {item_name}\n")
        name = input("What is your name? ")
        bid = float(input("What is your bid? $"))
        bids[name] = bid
    else:
        should_continue = False
highest_bidder = ""
highest_bid = 0
for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        highest_bidder = bidder 
print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}.")

