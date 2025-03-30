from pprint import pprint
from requests import get, post, delete

pprint(get('http://127.0.0.1:8080/api/v2/users').json())
# Какие пользователи есть сейчас

pprint(get('http://127.0.0.1:8080/api/v2/users/2').json())
# Правильное получение пользователя

pprint(get('http://127.0.0.1:8080/api/v2/users/100').json())
# Нет такого пользователя

pprint(post('http://127.0.0.1:8080/api/v2/users', json={}).json())
# Пустой запрос

pprint(post('http://127.0.0.1:8080/api/v2/users', json={'name': 'Paul'}).json())
# Не все поля

pprint(post('http://127.0.0.1:8080/api/v2/users', json={'name': 'Paul', 'position': 'warrior',
                                                        'surname': 'Atreides', 'age': 17, 'address': 'dune',
                                                        'speciality': 'mystic',
                                                        'hashed_password': 'paul', 'email': 'paul@mars.org'}).json())
pprint(get('http://127.0.0.1:8080/api/v2/users/4').json())
# Правильный запрос

pprint(delete('http://127.0.0.1:8080/api/v2/users/999').json())
# Нет такого пользователя

pprint(delete('http://127.0.0.1:8080/api/v2/users/4').json())
# Правильное удаление
