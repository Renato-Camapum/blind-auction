from replit import clear
from art import logo
#this is an exercise using dictionary and loops. enjoy!
print(logo)
print("Welcome to the blind auction App.")

bidder_dict = {}
should_continue = True

def better_bid(bid_record):
    highest_bid = 0
    winner = ""
    for bids in bid_record:
        bid_amount = bid_record[bids]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bids
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while should_continue:
    name_bidder = input("what is your name: ")
    bid_bidder = int(input("what is your bid? $"))

    
    bidder_dict[name_bidder] = bid_bidder
        
    continue_bid = input("Is there any another bidder? Type 'yes' or 'no': ")   
    if continue_bid == "no":
        should_continue = False
    clear()
    better_bid(bidder_dict)
   
    
   
    
   
