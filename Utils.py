import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = ""


def Screen_cleaner():
    """
    clear the screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


