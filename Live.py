# This function has a person name as an input and returns a string in the following layout:
def welcome(name: str):
    return f"Hello {name} and welcome to the World of Games (WoG).Here you can find many cool games to play"


def load_game():
    # prints out the following text:
    choose_game = int(input("Please choose a game to play:"
                            "\n1. Memory Game - a sequence of numbers will appear for 1 second and you have "
                            "to guess it back"
                            "\n2. Guess Game - guess a number and see if you chose like the computer"
                            "\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS:\n"))

    # Get the level of difficulty
    game_level = int(input("Please choose game difficulty from 1 to 5: "))
