from flask import Flask, request
from flask_restful import Resource, Api
import requests
app = Flask(__name__)
api = Api(app)

class MyResource(Resource):
    def post(self):
        data = request.data
        dict = {'username1':'allengng', 'username2':'siushi'}
        final = []
        # Process data
        for i in range (1,3):
            f = requests.get('https://api.github.com/users/%s/keys' % dict.get('username%s' % i))
            final.append(f.text)

        return {'message': final}

api.add_resource(MyResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
