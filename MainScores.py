from flask import Flask, render_template
import Utils

app = Flask(__name__)


@app.route("/")
def score_server():
    try:
        with open(Utils.SCORES_FILE_NAME, 'r') as f:
            score = f.read()
        score_div = score
    except Exception as e:
        score_div = str(e)

    return render_template("/index.html", score_div=score_div)


app.run(host="0.0.0.0")
