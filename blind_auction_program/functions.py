import os


def get_bidder():
    """
    Gets name and bid amount from bidder and ensures bid amount is a whole number and not anything else
    :return: bidder name and bid amount
    """
    name = input("Please enter your name: ")
    bid = (input("Please enter your bid (round to nearest whole number): $"))
    while not bid.isnumeric():
        print("We only accept whole numbers.")
        bid = input("Please enter your bid rounded to the nearest whole number: $")
    return name, int(bid)


def continue_bidding():
    to_continue = input("Is there another bidder? Type 'yes' or 'no': ").lower()
    while to_continue not in ["yes", "no", ""]:
        to_continue = input("Please type either 'yes' or 'no': ").lower()
    return to_continue


def determine_winner(bid_dict):
    """
    Takes in dictionary of bidders/bid amounts and determines the winner
    :param bid_dict: dictionary of bidders as keys and their bid amounts as values
    :return: list of winner(s)
    """
    highest_bid = 0
    winner_list = []
    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]
        if highest_bid < bid_amount:
            highest_bid = bid_amount
            winner = bidder
            winner_list.clear()
        elif highest_bid == bid_amount:
            winner_list.append(bidder)
    winner_list.append(winner)
    return winner_list, highest_bid


def run_off(list, highest_bid):
    """
    Determines the winner if there is a tie in the auction
    :param list: list of tied players
    :param highest_bid: amount of the tying bid
    :return: list of winner(s) and the highest bid
    """
    tie_dict = {}
    for person in list:
        name = person
        bid = input(f"{name}, please enter your new bid: $")
        while not bid.isnumeric() or int(bid) <= highest_bid:
            if not bid.isnumeric():
                print("You already know the format. We only accept whole numbers.")
                bid = input("Please enter your new bid rounded to the nearest whole number: $")
                continue
            if int(bid) <= highest_bid:
                print(f"You must enter a bid greater than your previous bid of ${highest_bid}")
                bid = input(f"{name}, please enter your new bid: $")
                continue
        tie_dict[name] = int(bid)
        clear_console()
    winner_list, highest_bid = determine_winner(tie_dict)
    return winner_list, highest_bid


def clear_console():
    os.system('cls')