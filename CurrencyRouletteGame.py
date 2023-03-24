import random

import requests


def get_converted_amount(from_cur: str, to_curr: str, amount: int) -> float:
    # set API endpoint and parameters
    url = "https://api.apilayer.com/exchangerates_data/convert"

    params = {
        "from": from_cur,
        "to": to_curr,
        "amount": amount,
    }

    headers = {
        "apikey": "0fkkBNrT2NJZBItjUloDRCGShJW9uWEg"
    }

    # make API request
    response = requests.get(url, headers=headers, params=params)

    # parse response JSON and get exchange rate
    return round(response.json()["result"], 2)


def get_money_interval(difficulty: int, converted_amount: float) -> tuple:
    # Interval range
    interval_rate = converted_amount - (5 - difficulty), converted_amount + (5 - difficulty)
    return interval_rate


def generate_number():
    return random.randint(1, 100)


def get_guess_from_user(gen_number: float) -> float:
    """
    prompt a guess from the user to enter a guess of
    value to a given amount of USD
    """
    return float(input(f"Guess the value in NIS for {gen_number} USD: "))


def compare_results(user_guess: float, money_interval: tuple):
    """
    Check if user guess is inside the money interval range
    """
    return money_interval[0] <= user_guess <= money_interval[1]


def play(difficulty: int):
    # Generate number between 1 and 100
    gen_number = generate_number()

    # Convert number from USD to NIS
    converted_amount = get_converted_amount("usd", "ils", gen_number)

    # Get money interval
    money_interval = get_money_interval(difficulty, converted_amount)

    # Get user guess
    user_guess = get_guess_from_user(gen_number)

    if compare_results(user_guess, money_interval):
        print(f"You won. your guess {user_guess} NIS was inside the interval {money_interval}")
        return True
    else:
        print(f"You lost. your guess {user_guess} NIS was outside the interval {money_interval}")
        return False


play(3)
