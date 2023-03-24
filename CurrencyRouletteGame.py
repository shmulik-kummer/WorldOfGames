import requests


def get_converted_rate(from_cur: str, to_curr: str, amount: int) -> float:
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
    return response.json()["result"]


def get_money_interval(from_cur: str, to_cur: str, difficulty: int, amount: int) -> tuple:
    # Convert amount according to current currency rate
    converted_amount = get_converted_rate(from_cur, to_cur, amount)
    print(f"Converted amount = {converted_amount}")

    # Interval range
    interval_rate = converted_amount - (5 - difficulty), converted_amount + (5 - difficulty)
    print(f"Interval rate = {interval_rate}")
    return interval_rate


get_money_interval("usd", "ils", 4, 5)
