import flask

app = flask.Flask(__name__)

@app.route("/exercises")
def products_page():
    exercises_content = open('exercises.md', 'r').read()
    return flask.render_template_string(exercises_content)

@app.route("/chapter")
def main_page():
    chapter_content = open('chapter.md', 'r').read()
    return flask.render_template_string(chapter_content)

app.run(debug=True, port=8080)