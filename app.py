import ast
from flask import Flask, render_template, request

import GuessGame
import MemoryGame

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('chooseGame.html')


@app.route('/play', methods=['POST'])
def play():
    choice = int(request.form['game'])
    level = int(request.form['level'])

    # Memory game
    if choice == 1:
        # Generate list of random numbers according to difficulty level
        random_numbers = MemoryGame.generate_sequence(level)
        return render_template('memoryGame.html', level=level, numbers=random_numbers)

    # Guess game
    elif choice == 2:
        # generate a random number between 1 - difficulty level
        secret_number = GuessGame.generate_number(level)
        return render_template('guessGame.html', level=level, number=secret_number)


@app.route('/guess', methods=['POST'])
def process_guess():
    guesses = [int(guess) for guess in request.form.getlist('guesses[]')]
    numbers = ast.literal_eval(request.form.get('numbers'))

    # Compare the guesses with the numbers
    if MemoryGame.is_list_equal(numbers, guesses):
        return render_template("memoryWin.html")
    else:
        return render_template("memoryLose.html")


@app.route('/secret_guess', methods=['POST'])
def process_secret_guess():
    guess = request.form.get("guess")
    secret_number = request.form.get('number')
    print(f"guess = {guess}")
    print(f"Secret number = {secret_number}")

    #     Compare the guess wth the secret number
    if GuessGame.compare_results(guess, secret_number):
        return "You guess correct"
    else:
        return f"you are wrong. the secret number is: {secret_number}"


if __name__ == '__main__':
    app.run(debug=True)
