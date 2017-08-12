from flask import Flask, request
from flask_restful import Resource, Api
import json
import requests
app = Flask(__name__)
api = Api(app)

class MyResource(Resource):
    def post(self):

        usernames = []
        keys = []

        # Load the data given by the client
        dict = json.loads(request.data)
        name = dict.get('user-name-list')

        # The outline for the output back to the client
        dict2 = {'id': '', 'key': ''}
        dict1 = {'name': '', 'id-key': dict2}
        dict0 = {'user-keys' : dict1}

        # Begin looping and get the ID and Key for the given GitHub usernames
        for i in range(0, len(name)):
            f = requests.get('https://api.github.com/users/%s/keys' % name[i])

            # Check to see if it was successful and returned somemthing
            if(f.status_code == requests.codes.ok):
                dict1['name'] = name[i]
                dictResult = f.json()

                #keys.append(f.text)
                #keys.append(f.status_code)
                for i in dictResult:
                    dict2['id'] = i['id']
                    dict2['key'] = i['key']

                usernames.append(dict0.items())
        return {'message': usernames}

api.add_resource(MyResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
