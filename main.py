from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route('/result/<nickname>/<int:level>/<float:rating>')
def choice(nickname, level, rating):
    return render_template("index.html", nickname=nickname, level=level, rating=rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
