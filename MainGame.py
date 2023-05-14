import CurrencyRouletteGame
import GuessGame
import MemoryGame
import Score


def welcome(name: str) -> str:
    """
    This function takes a person's name as an input and returns a string welcoming them to the World of Games.
    """
    return f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play."


def load_game():
    """
    This function prompts the user to choose a game to play and start the relevant game.
    """
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS:")

    while True:
        try:
            choice = int(input())
            if choice in [1, 2, 3]:
                break
        except ValueError:
            pass
        print("Invalid choice. Please enter 1, 2, or 3: ")

    print("Please choose game difficulty from 1 to 5: ")

    while True:
        try:
            level = int(input())
            if 1 <= level <= 5:
                break
        except ValueError:
            pass
        print("Invalid level. Please enter a number between 1 and 5: ")

    # if choice == 1:
    #     if MemoryGame.play(level):
    #         Score.add_score(level)
    #
    # elif choice == 2:
    #     if GuessGame.play(level):
    #         Score.add_score(level)
    # else:
    #     if CurrencyRouletteGame.play(level):
    #         Score.add_score(level)

    play_game(choice, level)


def play_game(choice, level):
    game_functions = {
        1: MemoryGame.play,
        2: GuessGame.play,
        3: CurrencyRouletteGame.play
    }
    result = game_functions[choice](level)
    if result:
        Score.add_score(level)


print(welcome("Shmulik"))
load_game()
