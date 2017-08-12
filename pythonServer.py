from flask import Flask, request
from flask_restful import Resource, Api
import json
import requests
app = Flask(__name__)
api = Api(app)

class MyResource(Resource):
    def post(self):
        """
        #data = request.data
        #dict = {'username1':'allengng', 'username2':'siushi'}
        final = []
        # Process data
        for i in range (1,3):
            f = requests.get('https://api.github.com/users/%s/keys' % dict.get('username%s' % i))
            final.append(f.text)

        return {'message': final}
        """
        usernames = []
        keys = []
        # Load the data given by the client
        dict = json.loads(request.data)
        name = dict.get('user-name-list')
        #for j in range(0, len(name)):
        dict2 = {'id': '', 'key': ''}
        dict1 = {'name': '', 'id-key': dict2 }
        dict0 = {'user-keys' : dict1}



        for i in range(0, len(name)):
            #usernames.append(name[i])
            f = requests.get('https://api.github.com/users/%s/keys' % name[i])

            # Check to see if it was successful and returned somemthing
            if(f.status_code == requests.codes.ok):
                dict1['name'] = name[i]
                dictResult = f.json()

                keys.append(f.text)
                keys.append(f.status_code)
                for i in dictResult:
                    dict2['id'] = i['id']
                    dict2['key'] = i['key']
                usernames.append(dict0)
        return {'message': usernames}

api.add_resource(MyResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
