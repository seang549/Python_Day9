from art import logo

def clear():  # Prints 50 blank lines
    print("\n" * 50)
#HINT: You can call clear() to clear the output in the console.
clear()

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if int(bid_amount) > int(highest_bid):
            highest_bid = bid_amount
            winner = bidder
        
    print(f"The highest bidder is {winner} at ${highest_bid}.")

while not bidding_finished:
    user_name = input("What is your name?\n")
    user_bid = input("Name your price!\n$")
    bids[user_name] = user_bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == 'yes':
        clear()
    elif should_continue == 'no':
        bidding_finished = True

find_highest_bidder(bids)
