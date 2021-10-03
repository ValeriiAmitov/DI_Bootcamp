from flask import Flask, render_template

app = Flask(__name__)

users = ['Valerii']


@app.route('/')
def blog_users():
    return render_template('homepage.html', blog_users=users)


if __name__ == "__main__":
    app.run(debug=True, port=5000)