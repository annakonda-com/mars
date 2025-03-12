from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/galery/', methods=['POST', 'GET'])
def index1():
    if request.method == 'POST':
        f = request.files['file']
        print(f.read())
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
