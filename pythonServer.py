from flask import Flask, request
from flask_restful import Resource, Api
import requests
app = Flask(__name__)
api = Api(app)

class MyResource(Resource):
    def post(self):
        data = request.data
        # Process data
        f = requests.get('https://api.github.com/users/%s/keys' % data)
        return {'message': f.text}

api.add_resource(MyResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
