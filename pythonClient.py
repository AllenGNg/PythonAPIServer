# Creating the intial file for the client
import json
import requests
import pprint
url = 'http://127.0.0.1:5000'
# Names of the GitHub Usernames you want to search.
dict = {'user-name-list': ['allengng', 'mjluck']}
data = json.dumps(dict)
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=data, headers=headers)
pprint.pprint(response.json()['message'])
