class Artwork:
    def __init__(self, title, artist, year_created):
        self.title = title
        self.artist = artist
        self.year = year_created

    def get_info(self):
        # Cette méthode retourne un dictionnaire contenant les informations de base de l'œuvre.
        artwork_info = {
            "Title": self.title,
            "Artist": self.artist,
            "Year": self.year
        }
        return artwork_info

    def update_info(self, title, artist, year_created):
        # Cette méthode permet de mettre à jour les informations de l'œuvre.
        self.title = title
        self.artist = artist
        self.year_created = year_created
    


       

        