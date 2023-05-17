from random import randint


def generate_number(difficulty):
    return randint(1, difficulty)


def get_guess_from_user(difficulty):
    guess = int(input(f"Please guess a number between 1 and {difficulty}: "))
    if guess < 1 or guess > difficulty:
        raise Exception(f"Sorry, numbers between 1 and {difficulty} only")
    return guess


def compare_results(first_number, second_number):
    return first_number == second_number


def play(difficulty):
    try:
        secret_number = generate_number(difficulty)
        user_guess = get_guess_from_user(difficulty)
        result = compare_results(user_guess, secret_number)
        return result
    except BaseException as e:
        print(e)
