from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


class Dev(Resource):
    def get(self, id):
        return {'id': id, 'name':'test'}
    
    def post(self, id):
        dados = json.loads(request.data)
        print(dados)
        return 'post'

api.add_resource(Dev, '/dev/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)