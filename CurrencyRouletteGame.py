import random
import requests

API_URL = "https://api.apilayer.com/exchangerates_data/convert"
API_KEY = "0fkkBNrT2NJZBItjUloDRCGShJW9uWEg"
MONEY_RANGE_DIFFICULTY_FACTOR = 5


def get_converted_amount(from_cur: str, to_curr: str, amount: int) -> float | None:
    params = {
        "from": from_cur,
        "to": to_curr,
        "amount": amount,
    }

    headers = {
        "apikey": API_KEY
    }

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print("An error occurred while retrieving exchange rate data:", e)
        return None

    return round(response.json()["result"], 2)


def get_money_interval(difficulty: int, converted_amount: float) -> tuple:
    """
    Calculate the money interval for the given difficulty and converted amount.
    """
    money_range = MONEY_RANGE_DIFFICULTY_FACTOR - difficulty
    interval_start = converted_amount - money_range
    interval_end = converted_amount + money_range
    return interval_start, interval_end


def generate_number():
    """
    Generate number between 1-100
    """
    return random.randint(1, 100)


def get_guess_from_user(gen_number: float) -> float:
    """
    prompt a guess from the user to enter a guess of
    value to a given amount of USD
    """
    while True:
        try:
            user_guess = float(input(f"Guess the value in NIS for {gen_number} USD: "))
            return user_guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")


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
