from art import logo
import functions as f


def blind_auction():
    bid_dict = {}
    end_of_auction = False

    print(logo)
    print("Welcome to the blind auction!")

    while not end_of_auction:
        name, bid = f.get_bidder()
        bid_dict[name] = bid
        to_continue = f.continue_bidding()
        if to_continue == 'yes':
            f.clear_console()
            end_of_auction = False
        else:
            winner_list, winning_bid = f.determine_winner(bid_dict)
            while len(winner_list) > 1:
                print("There was a tie! We proceed to a runoff between: ")
                for person in winner_list:
                    print(person)
                    if person != winner_list[-1]:
                        print("and")
                winner_list, winning_bid = f.run_off(winner_list, winning_bid)
            print(f"\nThe winner is {winner_list[0]} with a bid of ${winning_bid}!")
            end_of_auction = True

    replay_auction = input("\nWould you like to participate in another auction?\nType 'y' or 'n': ").lower()
    while replay_auction != 'y' and replay_auction != 'n':
        replay_auction = input("Please input either 'y' or 'n': ").lower()
    if replay_auction == 'y':
        blind_auction()
    else:
        return


blind_auction()