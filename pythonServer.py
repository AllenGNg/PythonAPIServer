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
        got200 = False
        got429 = False

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
                    got200 = True

            # If the username is not found (404), set its ID and Key as 'N/A'.
            elif(f.status_code == 404):
                outputDict[nameList[i]] = [{'id': 'N/A', 'key': 'N/A'}]

            elif(f.status_code == 429):
                got429 = True

        # Sends the dictionary with all usernames, keys, and IDs to the client.
        # Checks certain cases, and responds accordingly.
        if(got200 == True and got429 == False):
            return {'keyData': outputDict, 'Return Message': 'No Errors Occured.' }
        elif(got200 == True and got429 == True):
            return{'keyData': outputDict, 'Return Message': 'All names were processed but due to the limit of API calls being met, not all keys and IDs may be shown.'}
        elif(got200 == False and got429 == True):
            return {'keyData': [], 'Return Message': 'No names were processed, the amount of calls to the GitHub API has been reached. Please wait until your limit has been reset.'}

api.add_resource(MyResource, '/getKeys')

if __name__ == '__main__':
    app.run(debug=True)
