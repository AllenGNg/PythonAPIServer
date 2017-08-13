from flask import Flask, request
from flask_restful import Resource, Api
import json
import requests
import pprint

app = Flask(__name__)
api = Api(app)

class MyResource(Resource):
    def post(self):

        # Load the data given by the client,
        inputDict = json.loads(request.data)
        nameList = inputDict.get('user-name-list')

        outputDict = {}
        dictList = []

        # Begin looping and get the ID and Key for the given GitHub usernames
        for i in range(0, len(nameList)):
            f = requests.get('https://api.github.com/users/%s/keys' % nameList[i])

            # Check to see if it was successful and returned something.
            if(f.status_code == requests.codes.ok):
                responseData = f.json()

                # Incase the user has multiple keys and IDs.
                # Counter used for creating the key for the first id and key found
                counter = 1
                for j in responseData:
                    # If this is the first run through, it will create the key which is the username.
                    if(counter == 1):
                        outputDict[nameList[i]] = [{'id': j['id'], 'key': j['key']}]
                    # If there are more than one key and id, it will then append them to the end of the list for that username.
                    else:
                        dictList = outputDict.get(nameList[i])
                        dictList.append({'id': j['id'], 'key': j['key']})
                    counter = counter + 1

            # If the username is not found (404), set its ID and Key as 'N/A'.
            elif(f.status_code == 404):
                outputDict[nameList[i]] = [{'id': 'N/A', 'key': 'N/A'}]

        # Sends the dictionary with all usernames, keys, and IDs to the client.
        return {'message': outputDict}

api.add_resource(MyResource, '/')

if __name__ == '__main__':
    app.run(debug=False)
