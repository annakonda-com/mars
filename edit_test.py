import requests
from pprint import pprint

api_server = "http://127.0.0.1:8080/api/jobs/0"
response = requests.get(api_server)
pprint(response.json())
# Проверим какие работы есть сейчас

response = requests.post(api_server, json={}).json()
pprint(response)
# Пустой запрос

response = requests.post(api_server, json={
    'job': 'Работа',
    'team_leader': '3',
    'work_size': '3',
    'collaborators': '2',
}).json()
pprint(response)
# Переданы не все обязательные параметры

response = requests.post(api_server, json={
    'job': 'Работа',
}).json()
pprint(response)
# Переданы не все обязательные параметры

response = requests.post(api_server, json={
    'job': 'Строительствоо',
    'team_leader': '1',
    'work_size': '33',
    'collaborators': '2',
    'is_finished': True,
}).json()
pprint(response)

response = requests.get(api_server).json()
pprint(response)
# Работа изменилась