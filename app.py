from flask import Flask, jsonify, request
import json

app = Flask(__name__)

class Painting:
    def __init__(self, title, artist, year_created,painting_style):
        self.title = title
        self.artist = artist
        self.year_created = year_created
        self.painting_style = painting_style

    def get_info(self):
        return {
            "Title": self.title,
            "Artist": self.artist,
            "Year_created": self.year_created,
            "Painting_style": self.painting_style,
        }
    
def load_paintings():
    with open("paintings.json", "r") as f:
        global paintings_data
        paintings_data = json.load(f)
app.before_request(load_paintings)

@app.route("/artwork/paintings/<name>", methods=["GET"])
def get_painting(name):
    painting_found = False
    painting_info = None

    for painting_data in paintings_data:
        if painting_data["title"] == name:
            painting_found = True

            # Création directe de l'objet Painting :
            painting_obj = Painting(
                title=painting_data["title"],
                artist=painting_data["artist"],
                year_created=painting_data["year_created"],
                painting_style=painting_data["painting_style"],
            )

            painting_info = painting_obj.get_info()
            break

    if painting_found:
        return jsonify(painting_info)
    else:
        return jsonify({"message": "item not found"})     

if __name__ == "__main__":
    app.run(host="localhost", port=8888)     
