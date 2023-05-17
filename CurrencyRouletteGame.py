import requests

currency_api = "https://api.exchangerate.host/convert?from=USD&to=ILS"


def get_money_interval(amount, difficulty):
    global currency_api
    response = requests.get(currency_api).json()
    if not response or not response['success']:
        raise Exception("Under Maintenance")
    return amount * response['result'] - (5 - difficulty), amount * response['result'] + (5 - difficulty)


def get_guess_from_user():
    return int(input('Please enter your guess: '))


def play(difficulty):
    try:
        amount = int(input('Please enter amount of USD between 1 and 100: '))
        if 1 > amount or amount > 100:
            print("Wrong Amount")
        else:
            guess_range = get_money_interval(amount, difficulty)
            user_guess = get_guess_from_user()
            return guess_range[0] <= user_guess <= guess_range[1]
    except BaseException as e:
        print(e)

