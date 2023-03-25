# The purpose of memory game is to display an amount of random numbers to the users for 0.7
# seconds and then prompt them from the user for the numbers that he remember. If he was right
# with all the numbers the user will win otherwise he will lose.

import random


def generate_sequence(difficulty):
    """
    generate a list of random numbers between 1 and 101. The list
    length will be difficulty.
    """
    numbers = [random.randint(1, 101) for _ in range(difficulty)]
    return numbers


def is_list_equal(rand_list, user_list):
    """
    Compare two lists if they are equal. The function will return
    True / False.
    """
    return all(x == y for x, y in zip(rand_list, user_list))
