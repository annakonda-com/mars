import requests
from pprint import pprint
from datetime import datetime

api_server = "http://127.0.0.1:8080/api/jobs"
response = requests.get(api_server).json()
pprint(response)
# Проверим какие работы есть сейчас

api_server = "http://127.0.0.1:8080/api/jobs"
response = requests.post(api_server).json()
pprint(response)
# Пустой запрос
api_server = "http://127.0.0.1:8080/api/jobs"
response = requests.get(api_server).json()
pprint(response)
# Проверим какие работы есть сейчас: ничего не поменялось

params = {
    'job': 'Работа',
    'team_leader': 'не число',
    'work_size': '3',
    'collaborators': '2',
    'is_finished': '0'
}
api_server = "http://127.0.0.1:8080/api/jobs"
response = requests.post(api_server, params=params).json()
pprint(response)
# В одном из параметров передан неправильный тип
api_server = "http://127.0.0.1:8080/api/jobs"
response = requests.get(api_server).json()
pprint(response)
# Проверим какие работы есть сейчас: ничего не поменялось

params = {
    'job': 'Работа',
    'team_leader': '3',
    'work_size': '3',
    'collaborators': '2',
}
api_server = "http://127.0.0.1:8080/api/jobs"
response = requests.post(api_server, params=params).json()
pprint(response)
# Переданы не все обязательные параметры
api_server = "http://127.0.0.1:8080/api/jobs"
response = requests.get(api_server).json()
pprint(response)
# Проверим какие работы есть сейчас: ничего не поменялось

params = {
    'job': 'Строительство',
    'team_leader': '2',
    'work_size': '3',
    'collaborators': '2',
    'is_finished': '0',
    'start_date': str(datetime.now)
}
api_server = "http://127.0.0.1:8080/api/jobs"
response = requests.post(api_server, params=params).json()
pprint(response)
# Переданы не все параметры
api_server = "http://127.0.0.1:8080/api/jobs"
response = requests.get(api_server).json()
pprint(response)
# Проверим какие работы есть сейчас: ничего не поменялось