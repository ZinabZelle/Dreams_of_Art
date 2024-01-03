from flask import Flask, jsonify
from main.Artwork import Artwork
from main.Sculpture import Sculpture
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

class SculptureManager:
    def __init__(self):
        self.sculptures = self.load_data()

    def load_data(self):
        with open('data/sculptures.json', 'r') as file:
            sculptures_data = json.load(file)

        sculptures = [Sculpture(**sculpture) for sculpture in sculptures_data]

        return sculptures

    def get_sculpture_by_name(self, name):
        for sculpture in self.sculptures:
            if sculpture.title == name:
                return sculpture
        return None


sculpture_manager = SculptureManager()

@app.route('/artwork/paintings/<name>', methods=['GET'])
def get_painting_info(name):
    painting = painting_manager.get_painting_by_name(name)

    if painting:
        return jsonify(painting.get_info())
    else:
        return jsonify({'message': 'Item not found'})
    
@app.route('/artwork/sculptures/<name>', methods=['GET'])
def get_sculpture_info(name):
    sculpture = sculpture_manager.get_sculpture_by_name(name)

    if sculpture:
        return jsonify(sculpture.get_info())
    else:
        return jsonify({'message': 'Sculpture not found'})

if __name__ == '__main__':
    app.run(port=8888)
