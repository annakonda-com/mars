from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/mars_explorer.db")

if __name__ == '__main__':
    # app.run(port=8080, host='127.0.0.1')
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.set_password('captain')
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Виггин"
    user.name = "Эндер"
    user.age = 12
    user.position = "Командор"
    user.speciality = "звёздные баталии"
    user.address = "Циолковского 32"
    user.email = "ender_chmo@mars.org"
    user.set_password('QQQ.shift')
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Атрейдс"
    user.name = "Пол"
    user.age = 15
    user.position = "маменькин сынок"
    user.speciality = "Езда на червях"
    user.address = "Кайтайн"
    user.email = "Harkonenn_is_bullshift@mars.org"
    user.set_password('Worms_are_cool')
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Купер"
    user.name = "Джозеф"
    user.age = 333
    user.position = "капитан звездодёта"
    user.speciality = "плакать"
    user.address = "Чёрная дыра"
    user.email = "i_love_merf@mars.org"
    user.set_password('iwanttogetback')
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
