from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/game', methods=['POST'])
def game():
    choice = int(request.form['game'])
    level = int(request.form['level'])
    if choice == 1:
        return render_template('memorygame.html', level=level)

    # Add code for other games here
    return 'Game Over'


if __name__ == '__main__':
    app.run(debug=True)
