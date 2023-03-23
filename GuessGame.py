# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty. The game will get a number input from the
import random


def play(difficulty):
    # Generate number between 1 and dif level
    secret_number = generate_number(difficulty)

    #    Input guess from user
    user_guess = get_guess_from_user(difficulty)

    #     Compare results
    if compare_results(user_guess, secret_number):
        print("You guess correct. you won")
        return True
    else:
        print(f"You are wrong. the number is: {secret_number}. you lost")
        return False


def generate_number(difficulty):
    """
    generate number between 1 to difficulty and save it to
    secret_number.
    """
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    """
    prompt the user for a number between 1 to difficulty and
    return the number.
    """
    number = int(input(f"Choose a number between 1 to {difficulty}: "))
    return number


def compare_results(user_guess, rand_number):
    """
    compare the secret generated number to the one prompted
    by the get_guess_from_user.
    """
    return user_guess == rand_number
