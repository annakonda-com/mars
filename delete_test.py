import requests
from pprint import pprint

api_server = "http://127.0.0.1:8080/api/jobs"
response = requests.get(api_server)
pprint(response.json())
# Проверим какие работы есть сейчас

response = requests.delete(api_server + '/999').json()
pprint(response)
# Нет такой новости

response = requests.delete(api_server + '/2024').json()
pprint(response)
# Нет такой новости

response = requests.delete(api_server + '/1').json()
pprint(response)
# Правильный запрос

response = requests.get(api_server).json()
pprint(response)
# Работа удалилась