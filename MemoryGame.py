import random
from time import sleep


max_number = 101
show_list_time = 1


def generate_sequence(difficulty):
    return random.sample(range(1, max_number), difficulty)


def get_list_from_user(difficulty):
    input_list = input("Type the numbers you remember: ").split(' ')
    users_list = [int(x) for x in input_list]
    if len(users_list) != difficulty:
        False
    else:
        return users_list


def is_list_equal(first_list, second_list):
    a = set(first_list)
    b = set(second_list)
    return a == b


def play(difficulty):
    try:
        random_list = generate_sequence(difficulty)
        print("Remember these numbers: ")
        print(random_list, end="\r")
        sleep(show_list_time)
        user_list = get_list_from_user(difficulty)
        if user_list:
            compare = is_list_equal(user_list, random_list)
            return compare
        else:
            return False
    except BaseException as e:
        print(e)

