from flask import Flask, redirect, render_template, request
import os

app = Flask(__name__)


@app.route('/galery/', methods=['POST', 'GET'])
def index1():
    images = os.listdir('./static/img')
    if request.method == 'POST':
        f = request.files['file']
        save = f.read()
        new_name = images[-1].split('.')[0][:-1] + str(int(images[-1].split('.')[0][-1]) + 1)
        with open(f'static/img/{new_name}', mode="wb") as file:
            file.write(save)
        images = os.listdir('./static/img')
    return render_template("index.html", images=images[1:])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
