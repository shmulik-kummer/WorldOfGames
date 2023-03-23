import ast
from flask import Flask, render_template, request
import MemoryGame

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('chooseGame.html')


@app.route('/play', methods=['POST'])
def play():
    choice = int(request.form['game'])
    level = int(request.form['level'])

    if choice == 1:
        random_numbers = MemoryGame.generate_sequence(level)
        return render_template('memoryGame.html', level=level, numbers=random_numbers)


@app.route('/guess', methods=['POST'])
def process_guess():
    guesses = [int(guess) for guess in request.form.getlist('guesses[]')]
    numbers = ast.literal_eval(request.form.get('numbers'))

    # Compare the guesses with the numbers
    if MemoryGame.is_list_equal(numbers, guesses):
        return render_template("memoryWin.html")
    else:
        return render_template("memoryLose.html")


if __name__ == '__main__':
    app.run(debug=True)
