from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/example', methods=['GET'])
def example():
    data = {'message': 'Hello Dreams of Art'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
    
    
