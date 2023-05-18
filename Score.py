import Utils
from os.path import exists


def add_score(difficulty):
    score = difficulty * 3 + 5
    if not exists(Utils.SCORES_FILE_NAME):
        handler = open(Utils.SCORES_FILE_NAME, "w")
    else:
        handler = open(Utils.SCORES_FILE_NAME, 'r+')
        score += int(handler.read())
        handler.seek(0)

    handler.write(f'{str(score)}\n')
    handler.close()
