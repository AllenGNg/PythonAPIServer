# This implements the IDsandKeys API which returns the IDs and Public SSH Keys for the specified users.
from flask import Flask, request
from flask_restful import Resource, Api
import json
import requests
import pprint

app = Flask(__name__)
api = Api(app)

class MyResource(Resource):
    def post(self):

        # Dictionary to return to Client.
        outputDict = {}
        # List of IDs and Keys dictionary for users.
        dictList = []

        # Load the data passed by the client.
        inputDict = json.loads(request.data)
        nameList = inputDict.get('user-name-list')

        # Booleans to check if certain Status Codes were received.
        gotStatusCode200 = False
        gotStatusCode403 = False

        # Process all usernames.
        for i in range(0, len(nameList)):
            f = requests.get('https://api.github.com/users/%s/keys' % nameList[i])

            # Check to see if invoked API returns Status Code 200.
            if(f.status_code == requests.codes.ok):
                print(f.status_code)
                responseData = f.json()

                # Create the dictionary for each username.
                # Counter is used to insure that a single list of dictionaries is created for each user.
                counter = 1
                # If the user has more than one ID and Key, we will loop through until we have appended all the ID and Key pairs to that users dictionary.
                for j in responseData:
                    # Processing first ID and Key, create the list of dictionary for this user.
                    if(counter == 1):
                        outputDict[nameList[i]] = [{'id': j['id'], 'key': j['key']}]
                    # Add new ID and Key dictionary to the list.
                    else:
                        dictList = outputDict.get(nameList[i])
                        dictList.append({'id': j['id'], 'key': j['key']})
                    counter = counter + 1
                    gotStatusCode200 = True

            # If the username is not found (404), set its ID and Key as 'N/A'.
            elif(f.status_code == 404):
                outputDict[nameList[i]] = [{'id': 'N/A', 'key': 'N/A'}]
            # We are checking 403 instead of 429 since the GitHub API uses 403 instead of 429 when the API call limit has been reached.
            elif(f.status_code == 403):
                gotStatusCode403 = True

        # Return the dictionary with all usernames, keys, and IDs to the client.
        # This checks to see if we ran into any errors.
        if(gotStatusCode200 == True and gotStatusCode403 == False):
            return {'key-data': outputDict, 'info-message': 'All users processed.' }
        # This checks to see if we ran into the max number of GitHub API calls midway through a POST request.
        elif(gotStatusCode200 == True and gotStatusCode403 == True):
            return{'key-data': outputDict, 'info-message': 'All names were processed but due to the limit of API calls being met, not all keys and IDs may be shown.'}
        # This checks to see if we try sending a POST request after we have used all of our avaialbel API calls.
        elif(gotStatusCode200 == False and gotStatusCode403 == True):
            return {'key-data': ['N/A'], 'info-message': 'No names were processed, the amount of calls to the GitHub API has been reached. Please wait until your limit has been reset.'}

api.add_resource(MyResource, '/IDsandKeys')

if __name__ == '__main__':
    app.run(debug=True)
