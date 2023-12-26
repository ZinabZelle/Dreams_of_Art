from flask import Flask, jsonify
from main.Artwork import Artwork
import json

app = Flask(__name__)

class PaintingManager:
    def __init__(self):
        self.paintings = self.load_data()

    def load_data(self):
        with open('data/paintings.json', 'r') as file:
            paintings_data = json.load(file)

        paintings = [Artwork(**{k: v for k, v in painting.items() if k != "painting_style"}) for painting in paintings_data]

        return paintings

    def get_painting_by_name(self, name):
        for painting in self.paintings:
            if painting.title == name:
                return painting
        return None

painting_manager = PaintingManager()

@app.route('/artwork/paintings/<name>', methods=['GET'])
def get_painting_info(name):
    painting = painting_manager.get_painting_by_name(name)

    if painting:
        return jsonify(painting.get_info())
    else:
        return jsonify({'message': 'Item not found'})

if __name__ == '__main__':
    app.run(port=8888)
