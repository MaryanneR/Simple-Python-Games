from art import logo
import random


def higher_or_lower(answer_num, num_to_check):
    """
    Checks to see if a given number is higher or lower than the answer number
    :param answer_num: number to judge `num_to_check` against
    :param num_to_check: number to check again `answer_num` to see if it is higher or lower in value
    :return: print statement telling player whether their guessed number is higher or lower than answer number
    """
    if answer_num == int(num_to_check):
        message = "win"
    elif answer_num > int(num_to_check):
        message = "higher"
    else:
        message = "lower"

    return message


def check_replay():
    """
    Asks if the player would like to play again
    :return: Return player response
    """
    to_play = input("Would you like to play again? Type 'y' or 'n': ").lower()

    while to_play != 'y' and to_play != 'n':
        to_play = input("Please enter either 'y' or 'n': ").lower()

    return to_play


def guessing_game():

    # Greeting
    print(logo)
    print("Welcome to Guess The Number!\nWhere you'll have to guess a number between 1 and 100.")
    mode = input("Do you want Easy Mode or Hard Mode? Type 'e' or 'h' to choose: ").lower()

    # Ensure that only 'e' or 'h' is accepted as inputs for `mode` variable
    while mode != 'e' and mode != 'h':
        mode = input("Please pick either 'e' for Easy Mode or 'h' for Hard Mode: ").lower()

    # Define `chances` based on Easy Mode or Hard Mode
    if mode == 'e':
        chances = 10
    else:
        chances = 5
    print(f"You have {chances} chances to guess the correct number")

    # generate random number between 1 and 100
    answer = random.randint(1, 100)

    while chances != 0:
        # Get user input
        guess = input("Guess a number: ")

        # Ensure that `guess` input is a whole number between 1 and 100
        while not guess.isnumeric() or int(guess) < 1 or int(guess) > 100:
            if not guess.isnumeric():
                guess = input("Please enter a valid whole number: ")
            else:
                guess = input("Please enter a number between 1 and 100: ")

        compare_num = higher_or_lower(answer, guess)

        if compare_num == "win":
            print(f"Your number: {guess}, Answer: {answer}\nYOU WIN!")
            replay = check_replay()
            if replay == "y":
                guessing_game()
            else:
                return
        else:
            chances -= 1

            if chances != 0:
                print(f"Guess again, a {compare_num} number this time.")
                print(f"You have {chances} chances left.")
            else:
                print(f"Ooh so close! The answer was: {answer}\nYOU LOSE!")
                replay = check_replay()
                if replay == "y":
                    guessing_game()
                else:
                    return


guessing_game()