# The purpose of this game is to display an amount of random numbers to the users for 0.7
# seconds and then prompt them from the user for the numbers that he remember. If he was right
# with all the numbers the user will win otherwise he will lose.

import os
import random
import time


def play(difficulty):
    print(f"Starting the memory game with difficulty level of {difficulty}")

    # Generate a list of random numbers
    rand_numbers = generate_sequence(difficulty)

    # Display the list of numbers for 0.7 seconds
    print(f"The list of numbers are: {rand_numbers} ")
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Ask the user to input the numbers
    user_numbers = get_list_from_user(difficulty)

    # Check if both lists are the same (user guess correctly)
    if is_list_equal(rand_numbers, user_numbers):
        print(f"you won. the correct numbers are:{user_numbers}")
        return True
    else:
        print(f"You lose. your numbers are: {user_numbers} but the correct numbers are: {rand_numbers}")
        return False


def generate_sequence(difficulty):
    """
    generate a list of random numbers between 1 and 101. The list
    length will be difficulty.
    """
    return [random.randint(1, 101) for _ in range(difficulty)]


def get_list_from_user(difficulty):
    """
    return a list of numbers prompted from the user. The list length
    will be in the size of difficulty.
    """
    numbers_list = []
    for i in range(difficulty):
        while True:
            try:
                number = int(input(f"Enter number {i + 1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        numbers_list.append(number)
    return numbers_list


def is_list_equal(rand_list, user_list):
    """
    Compare two lists if they are equal. The function will return
    True / False.
    """
    return all(x == y for x, y in zip(rand_list, user_list))
