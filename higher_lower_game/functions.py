import random
from game_data import data as d
import os
import sys


def clear():
    """
    Clears console
    """
    os.system('cls')


def starts_with_vowel(text):
    text = text.lower()
    if text.startswith('a') or text.startswith('e') or text.startswith('i') or text.startswith('o') or text.startswith('u'):
        return True
    else:
        return False



def select_b(selection_a):
    """
    Chooses a random number in a range that is not the same as `selection_a`
    :param selection_a: a previously chosen random number
    :return: returns a random number in a range that is not equal to `selection a`
    """
    b = random.randint(0, 49)
    while selection_a == b:
        b = random.randint(0, 49)
    return b


def person(select_num):
    """
    Returns value from `d` dictionary that corresponds to select_num index value
    :param select_num: index value
    :return: returns value from keys (name, follower_count, description, country)
    """
    name = d[select_num]['name']
    follower_count = d[select_num]['follower_count']
    description = d[select_num]['description']
    country = d[select_num]['country']
    if country.startswith('U'):
        country = f"the {country}"
    if starts_with_vowel(description):
        description = f"an {description}"
    else:
        description = f"a {description}"
    return name, follower_count, description, country


def a_or_b():
    """
    Gets input from player and only accepts values of 'A' or 'B' (is not case-sensitive)
    :return: valid guess of 'A' or 'B'
    """
    guess = input("Which one has more followers? A or B?: ").lower()
    while guess != 'a' and guess != 'b':
        guess = input("Please type either A or B: ").lower()
    return guess


def most_followers(num_a, num_b):
    """
    Calculates whether num_a or num_b is larger
    :param num_a: follower count of A
    :param num_b: follower count of B
    :return: returns either `a` or `b`,
    """
    if num_a > num_b:
        return "a"
    else:
        return "b"


def replay():
    """
    Asks player if they would like to play again; only accepts valid answers
    :return: closes program if player does not want to play again
    """
    another_round = input("\nWould you like to play again? Type 'y' or 'n': ").lower()
    while another_round != 'y' and another_round != 'n':
        another_round = input("Please pick either 'y' or 'n': ").lower()

    if another_round == 'n':
        return sys.exit("Thank you for playing!")
    else:
        return