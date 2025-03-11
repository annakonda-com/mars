from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route('/choice/<planet>')
def choice(planet):
    return render_template("index.html", title="Варианты выбора", planet=planet)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
