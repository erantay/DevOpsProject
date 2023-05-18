import Utils
from flask import Flask, request

app = Flask("WorldOfGames")


@app.route('/score', methods=['GET'])
def score_server():
    try:
        handler = open(Utils.SCORES_FILE_NAME, 'r')
        score = handler.read()
        h1_content = f'The score is <div id="score">{score}</div>'
    except Exception as e:
        h1_content = f'<div id="score" style="color:red">{e}</div>'

    html = f'''
                <html>
                    <head>
                    <title>Scores Game</title>
                    </head>
                    <body>
                    <h1>{h1_content}</h1>
                    </body>
                </html>'''
    return html


app.run(host="0.0.0.0", port=8080, debug=False)