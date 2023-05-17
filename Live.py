import GuessGame
import MemoryGame
import CurrencyRouletteGame


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game():
    game = input(f'''Please choose a game to play:
            \r\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
            \r\t2. Guess Game - guess a number and see if you chose like the computer
            \r\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n\n\r>>> ''')

    if not game.isdigit() or int(game) not in range(1, 4):
        print('Invalid Game Choice')
    else:
        difficulty = int(input("Please choose game difficulty from 1 to 5: "))
        if difficulty not in range(1, 6):
            print('Invalid Level Choice')
        elif game == '1':
            result = MemoryGame.play(difficulty)
        elif game == '2':
            result = GuessGame.play(difficulty)
        elif game == '3':
            result = CurrencyRouletteGame.play(difficulty)

        if result:
            print('WIN')
        else:
            print('LOSS')
