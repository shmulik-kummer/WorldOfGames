from flask import Flask
import Utils

app = Flask(__name__)


@app.route("/")
def score_server():
    try:
        with open(Utils.SCORES_FILE_NAME, 'r') as f:
            score = f.read()
        score_div = f'<div id="score">{score}</div>'
    except Exception as e:
        score_div = f'<div id="score" style="color:red">{str(e)}</div>'

    html = f"""<html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1>The score is: {score_div}</h1>
</body>
</html>"""
    return html


app.run(host="0.0.0.0")