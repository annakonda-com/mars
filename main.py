from flask import Flask, redirect, render_template, request, url_for
import os
import json
from data import db_session
from data.users import User
from data.jobs import Jobs

from random import choice

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/mars_explorer.db")


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


@app.route('/member')
def member():
    with open('static/members.json', mode='r', encoding='utf8') as f:
        members = json.load(f)['members']
    curr_member = choice(members)
    return render_template('members.html', member=curr_member)


@app.route('/load_photo', methods=['POST', 'GET'])
def image_mars():
    if request.method == 'GET':
        return render_template('load_photo.html', image=-1)
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('load_photo.html', image=-1)
        else:
            with open('static/img/astro_photo', mode='wb') as f:
                f.write(request.files['file'].read())
            return render_template('load_photo.html', image='astro_photo')


@app.route('/carousel')
def carousel():
    images = os.listdir('./static/img')
    return render_template("index.html", images=images[1:])


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    names = dict()
    for job in jobs:
        user = db_sess.query(User).filter(User.id == job.team_leader).first()
        names[job.team_leader] = user.surname + ' ' + user.name
    return render_template("new_index.html", jobs=jobs, names=names, title="Марсиане")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
