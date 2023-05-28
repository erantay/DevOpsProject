import Utils
from flask import Flask, render_template

app = Flask("WorldOfGames", template_folder='templates')


@app.route('/score', methods=['GET'])
def score_server():
    try:
        handler = open(Utils.SCORES_FILE_NAME, 'r')
        score = handler.read()
        return render_template(
            "score.html.j2",
            score=score
        )
    except Exception as error:
        return render_template(
            "error.html.j2",
            error=error
        )


app.run(host="0.0.0.0", port=8080, debug=False)
