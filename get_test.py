import requests
from pprint import pprint

api_server = "http://127.0.0.1:8080/api/jobs"
response = requests.get(api_server).json()
pprint(response)
response = requests.get(api_server + '/2').json()
pprint(response)
response = requests.get(api_server + '/-33').json()
pprint(response)
response = requests.get(api_server + '/eshkere').json()
pprint(response)