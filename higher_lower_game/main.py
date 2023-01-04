import random
import functions as f
import art


def higher_lower_game():
    """
    A game of Higher and Lower, where the player guesses which person has the higher number of followers.
    """
    # Initial Setup
    end_game = False
    round_count = 0
    print(art.logo)

    # Initial Person A
    num_a = random.randint(0, 49)
    a = f.person(num_a)
    a_count = int(a[1])

    while not end_game:
        # Choosing Person B
        num_b = f.select_b(num_a)
        b = f.person(num_b)
        b_count = int(b[1])

        # Showing player the two options
        print(f"Compare A: {a[0]}, {a[2]}, from {a[3]}")
        print(art.vs)
        print(f"Against B: {b[0]}, {b[2]}, from {b[3]}")

        # Getting user input and calculating if it is correct
        guess = f.a_or_b()
        answer = f.most_followers(a_count, b_count)
        f.clear()
        print(art.logo)

        # Player either wins or loses
        if guess == answer:
            round_count += 1
            print(f"You're right! Current score: {round_count}")
            # Person B becomes Person A for the next round
            num_a = num_b
            a = b
            a_count = b_count
        else:
            print(f"Sorry, you're wrong! Final score: {round_count}")
            end_game = True
    f.replay()
    f.clear()
    higher_lower_game()


higher_lower_game()
