from flask import Flask, render_template, request

import MemoryGame
from MemoryGame import generate_sequence
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


if __name__ == '__main__':
    app.run(debug=True)
