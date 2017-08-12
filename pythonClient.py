# Creating the intial file for the client
import json
import requests
url = 'http://127.0.0.1:5000'
data = json.dumps({'fruit_1':'apple', 'fruit_2':'melon'})
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=data, headers=headers)
print(response.json()['message'])
