from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, welcome to the Flask API!'

@app.route('/hello', methods=['GET'])
def hello_route():
    return jsonify({"message": "Hello Dreams of Art"})

if __name__ == '__main__':
    app.run(port=8888) 