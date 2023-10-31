class collection:
    def __init__(self, name):
        self.name = name
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def get_collection(self):
        collection_info = {
            "Collection Name" : self.name,
            "Artwork": [artwork.get_info() for artwork in self.artworks]
        }        
        return collection_info
    
    def get_artwork_by_artist(self, artist_name):
        artist_artworks = [artwork.get_info() for artwork in self.artworks if artwork.artist == artist_name]
        return artist_artworks
    
    def get_artwork_by_style(self, style):
        style_artworks = [artwork.get_info() for artwork in self.artworks if hasattr(artwork, "painting_style") and artwork.painting_style == style]
        return style_artworks
        

    def calculate_total_value(self):
        totat_value = sum(artwork.value for artwork in self.artworks if hasattr(artwork, "value"))   
        return totat_value

    def sort_by_year(self, ascending=True) :
        self.artworks.sort(key=lambda artwork: artwork.year, reverse=not ascending)

    def remove_artwork(self, artwork):
        self.artworks.remove(artwork) 

    def clear_artwork_titles(self):
        return [artwork.title for artwork in self.artworks]      

    