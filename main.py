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


@app.route('/list_prof/<type>')
def list_prof(type):
    proffs = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
              'климатолог',
              'специалист по радиационной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
              'оператор марсохода', 'киберинжинер', 'штурман', 'пилот дронов']
    return render_template('list_prof.html', proffs=proffs, type=type)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
