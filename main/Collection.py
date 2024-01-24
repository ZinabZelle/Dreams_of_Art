from Artwork import Artwork

class Collection:
    def __init__(self, name):
        self.name = name
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def get_collection(self):
        collection_info = {
            "Collection Name" : self.name,
            "Artworks": []
        }  
        for artwork in self.artworks:
            collection_info["Artworks"].append(artwork.get_info())
        return collection_info