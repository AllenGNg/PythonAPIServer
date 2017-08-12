from flask import Flask, request
from flask_restful import Resource, Api
import json
import requests
app = Flask(__name__)
api = Api(app)

class MyResource(Resource):
    def post(self):

        # Final list to be returned to Client.
        usernames = []

        # Load the data given by the client,
        dict = json.loads(request.data)
        name = dict.get('user-name-list')

        # The outline for the output back to the client. NOT IN USE
        #dict2 = {'id': '', 'key': ''}
        #dict1 = {'name': '', 'id-key': dict2}
        #dict0 = {'user-keys' : dict1}

        #dict6 = {'Allen' : [{}]}

        # Begin looping and get the ID and Key for the given GitHub usernames
        for i in range(0, len(name)):
            dict5 = {'username': '', 'id': '', 'key': ''}

            f = requests.get('https://api.github.com/users/%s/keys' % name[i])

            # Check to see if it was successful and returned something
            if(f.status_code == requests.codes.ok):
                dict5['username'] = name[i]
                dictResult = f.json()

                for j in dictResult:
                    dict5['id'] = j['id']
                    dict5['key'] = j['key']
                    usernames.append(dict5.items())

        # Sends the list with all usernames, keys, and IDs to the client.            
        return {'message': usernames}

api.add_resource(MyResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
