# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty. The game will get a number input from the
import random


def generate_number(difficulty):
    """
    generate number between 1 to difficulty and save it to
    secret_number.
    """
    return random.randint(1, difficulty)


def compare_results(user_guess, rand_number):
    """
    compare the secret generated number to the one prompted
    by the get_guess_from_user.
    """
    return user_guess == rand_number
