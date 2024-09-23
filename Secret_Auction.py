bidding_on = True
bidders = []


def auction(name, amount):
    bidders.append({"name" : name, "amount" : amount})


def winner():
    amount_1 = 0
    winner_name = ""
    for element in bidders:
        if element["amount"] > amount_1:
            amount_1 = element["amount"]
            winner_name = element["name"]
    print(f"The auction winner is {winner_name} with ${amount_1} bid.")


while bidding_on:
    print("Welcome to Secret Auction.")
    bidder = input("What's your name? : ").lower()
    bid_amount = int(input("How much do you want to bid? : "))
    auction(bidder, bid_amount)
    if input("Are there any other bidders : ").lower() == "no":
        bidding_on = False

winner()
