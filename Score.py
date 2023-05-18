from os.path import exists


def add_score(difficulty):
    score = difficulty * 3 + 5
    if not exists('scores.txt'):
        handler = open("scores.txt", "w")
    else:
        handler = open('scores.txt', 'r+')
        score += int(handler.read())
        handler.seek(0)

    handler.write(f'{str(score)}\n')
    handler.close()
