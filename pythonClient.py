# Client for invoking the IDsandKeys Endpoint.
import json
import requests
import pprint

# Endpoint of the API to invoke.
url = 'http://127.0.0.1:5000/IDsandKeys'

# Usernames of the GitHub users you want to search.
dict = {'user-name-list': ['allengng']}
data = json.dumps(dict)
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=data, headers=headers)
print(response.json()['info-message'])
pprint.pprint(response.json()['key-data'])
