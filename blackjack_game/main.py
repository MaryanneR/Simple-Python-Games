from art import logo
import functions as f


def blackjack():
    global end_game
    end_game = False

    # Greeting
    print(logo)
    print("\nWelcome to blackjack!\n")
    rules = f.house_rules()
    print(rules)
    if rules != "":
        input("\nPress ENTER to continue: \n")

    while not end_game:
        # Deal two starting cards to player and computer
        player_hand = []
        player_score = 0
        player_aces_converted = 0

        dealer_hand = []
        dealer_score = 0
        dealer_aces_converted = 0

        # Deal two cards to player and computer
        print("You and the computer have each been dealt two cards\n")
        for value in range(0, 2):
            player_hand, player_score = f.deal_card(player_hand, player_score)
            dealer_hand, dealer_score = f.deal_card(dealer_hand, dealer_score)

        # Check if over 21 and if so, adjust "A" value
        player_score, player_aces_converted = f.convert_ace(player_hand, player_score, player_aces_converted)
        dealer_score, dealer_aces_converted = f.convert_ace(dealer_hand, dealer_score, dealer_aces_converted)

        # Check for blackjack
        first_round_win = False
        blackjack_check = f.is_blackjack(player_score, dealer_score)
        if blackjack_check == "d-blackjack":
            print(f"Dealer Blackjack! Computer's hand: {dealer_hand}\nYOU LOSE!")
            first_round_win = True
            end_game = True
        elif blackjack_check == "p-blackjack":
            print(f"Blackjack! Your hand: {player_hand}\nYOU WIN!")
            first_round_win = True
            end_game = True

        # If no first round Blackjack win, game continues
        if not first_round_win:
            print(f"Your hand: {player_hand}; current score: {player_score}")
            print(f"Computer's first card: {dealer_hand[0]}")

            # Ask if players would like another card and add card if "y" is chosen
            # Also evaluate if player hand goes over 21 - instant loss
            keep_dealing = True
            while keep_dealing:
                another_card = f.yes_or_no()
                if another_card == "y":
                    player_hand, player_score = f.deal_card(player_hand, player_score)
                    player_score, player_aces_converted = f.convert_ace(player_hand, player_score, player_aces_converted)
                    is_loss = f.instant_loss("player", player_hand, player_score)
                    if is_loss != "continue":
                        print(is_loss)
                        keep_dealing = False
                    else:
                        print(f"\nYour hand is {player_hand}; current score: {player_score}")
                else:
                    if player_score <= 21:
                        # Computer evaluates whether to draw more cards.
                        # If computer score < 16, computer draws cards. If computer score > 21, automatic win for player
                        while dealer_score < 16:
                            dealer_hand, dealer_score = f.deal_card(dealer_hand, dealer_score)
                            dealer_score, dealer_aces_converted = f.convert_ace(dealer_hand, dealer_score,
                                                                                dealer_aces_converted)
                        is_loss = f.instant_loss("dealer", dealer_hand, dealer_score)
                        if is_loss != "continue":
                            print(is_loss)
                        else:
                            end_message = f.calculate_winner(player_hand, player_score, dealer_hand, dealer_score)
                            eval_message = "\nLet's evaluate your hand and the computer's hand...\n"
                            print('*' * len(eval_message))
                            print(eval_message)
                            print('*' * len(eval_message))
                            print(end_message)
                        keep_dealing = False
        end_game = True
    f.replay()
    f.clear()
    blackjack()


round_num = 0
blackjack()
