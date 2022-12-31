import random
import hangman_words
import hangman_art

# Greeting
print(hangman_art.logo)
print()
print("Welcome to hangman. Are you ready to play?\nHere's your word: ")
print()

# Set lives
lives = 6

# Import list of words
word_list = hangman_words.word_list

# Choose word from list to be solution
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create list for guessed letters
guessed_letters = []

# Create empty list `display`
display = []

# display blanks
for i in range(word_length):
    display.append("_")
print(f"{' '.join(display)}")

end_of_game = False

while not end_of_game:
    # Show hangman progress
    print(hangman_art.stages[lives])

    # Get input from user
    guess = input("Guess a letter: ").lower()

    if guess == 'help' and len(guessed_letters) >= 1:
        print(sorted(guessed_letters))
        print(f"{' '.join(display)}")
    elif guess == 'help' and len(guessed_letters) < 1:
        print("You haven't guessed any letters yet. Please guess a letter.")
    elif len(guess) == 0:
        print("Please type in a letter before pressing 'Enter'")
    elif guess.isalpha() == False:
        print("Please type in a letter, no symbols or numbers will be accepted")
    elif len(guess) > 1:
        print("Please only type in one letter")
    else:

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Please try another letter.")
            print("If you need help remembering letters you have already guessed, type 'help'")
            print()
            print(f"{' '.join(display)}")

        if guess in chosen_word and guess not in guessed_letters:
            print(f"Nice! '{guess}' is in the word.")
            print()

        while guess not in guessed_letters:
            guessed_letters.append(guess)

            # Check if input letter is in chosen_word
            for position in range(word_length):
                letter = chosen_word[position]
                if guess == letter:
                    display[position] = letter

            if guess not in chosen_word:
                lives -= 1
                print(hangman_art.stages[lives])
                print(f"'{guess}' is not in the word.")
                if lives > 0:
                    print("You lose a life :/")
                print()

            if lives > 0:
                print(f"{' '.join(display)}")

            if "_" not in display:
                end_of_game = True
                print("Yay! You won!")

            if lives == 0:
                end_of_game = True
                print("GAME OVER")