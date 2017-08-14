# This implements the IDsandKeys API which returns the IDs and Public SSH Keys for the specified users.
from flask import Flask, request, abort
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
        # List of IDs and Keys dictionaries for users.
        dictList = []

        # Load the data passed by the client.
        # Try and Except block incase no request data was provided.
        try:
            inputDict = json.loads(request.data)
        except:
            return abort(400)

        nameList = inputDict.get('user-name-list')

        # Booleans to check if certain Status Codes were received.
        gotStatusCode200 = False
        gotStatusCode403 = False
        gotStatusCode404 = False

        # Process all usernames.
        # Checking if passed list is empty.
        if not nameList:
            return{'key-data': outputDict, 'info-message': 'No usernames were processed due to an empty list being passed'}

        for i in range(0, len(nameList)):
            f = requests.get('https://api.github.com/users/%s/keys' % nameList[i])

            # Check to see if invoked API returns Status Code 200.
            if(f.status_code == requests.codes.ok):
                responseData = f.json()

                # Create the dictionary for each username.
                # Counter is used to insure that a single list of dictionaries is created for each user.
                counter = 1
                # If the user has more than one ID and Key, we will loop through until we have appended all the ID and Key pairs to that user's dictionary.
                for j in responseData:
                    # Processing first ID and Key, create the list of dictionaries for this user.
                    if(counter == 1):
                        outputDict[nameList[i]] = [{'id': j['id'], 'key': j['key']}]
                    else:
                        # Add new ID and Key dictionary to the list.
                        dictList = outputDict.get(nameList[i])
                        dictList.append({'id': j['id'], 'key': j['key']})
                    counter = counter + 1
                    gotStatusCode200 = True

            # If the username is not found (404), set its ID and Key as 'N/A'.
            elif(f.status_code == 404):
                outputDict[nameList[i]] = [{'id': 'N/A', 'key': 'N/A'}]
                gotStatusCode404 = True
            # We are checking 403 instead of 429 since the GitHub API uses 403 instead of 429 when the API call limit has been reached.
            elif(f.status_code == 403):
                gotStatusCode403 = True

        # Return the dictionary with all usernames, keys, and IDs to the client.
        # This checks to see if we ran into any errors.
        if(gotStatusCode200 == True and gotStatusCode403 == False):
            return{'key-data': outputDict, 'info-message': 'All users processed.' }
        # This checks to see if we ran into the max number of GitHub API calls midway through a POST request.
        elif(gotStatusCode200 == True and gotStatusCode403 == True):
            return{'key-data': outputDict, 'info-message': 'All names were processed but due to the limit of API calls being met, not all keys and IDs may be shown.'}
        # This checks to see if we try sending a POST request after we have used all of our avaialbel API calls.
        elif(gotStatusCode200 == False and gotStatusCode403 == True):
            return{'key-data': ['N/A'], 'info-message': 'No names were processed, the amount of calls to the GitHub API has been reached. Please wait until your limit has been reset.'}
        # This checks to see if all of the usernames were not found.
        elif(gotStatusCode200 == False and gotStatusCode404 == True and gotStatusCode403 == False):
            return{'key-data': outputDict, 'info-message': 'All given usernames were not found'}

api.add_resource(MyResource, '/IDsandKeys')

if __name__ == '__main__':
    app.run(debug=True)
