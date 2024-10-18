from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
# create an API object
api = Api(app)

class Hello(Resource):
    def get(self):
        messages = "Hello world how are you?"
        return jsonify({'message': messages})
    
    def post(self):
        data_record = request.get_json()
        return jsonify({'data': data_record}), 201
    
class Square(Resource):
    def get(self, num):
        return jsonify({'the Sqare of '+ str(num) +' is ' : num**2})
    

api.add_resource(Hello, '/greetings/')
api.add_resource(Square, '/Square/<int:num>')

if __name__ == '__main__':
  app.run(debug = True)