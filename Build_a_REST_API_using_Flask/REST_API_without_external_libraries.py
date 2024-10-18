from  flask import Flask, jsonify, Request, request

# create Flask App
app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "Hello world how are you"
        return jsonify({'data': data})
    
@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
    return jsonify({'data': num**2})


if __name__ == '__main__':
    app.run(debug=True)