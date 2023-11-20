import json

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')

def hello():
    return 'Hello, Flask API!'

@app.route('/hello',methods=['GET'])
def hello_dreams_of_art():
    message = {"message": "Hello Dreams of Art"}
    return jsonify(message)

if __name__ == '__main__':
    app.run(port=8888)
    
    
