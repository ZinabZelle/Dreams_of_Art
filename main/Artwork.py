class Artwork:
    def __init__ ( self, title, artist, year ): 
        self.title = title
        self.artist = artist
        self.year = year
        

    def get_info(self):
        # Cette methode retourne un dictionnaire contenant les informations de base de l'oeuvre.
        artwork_info = {
            "Title" : self.title,
            "Artist" : self.artist,
            "Year" : self.year
        }
        return artwork_info
    
    def update_info(self, new_title, new_artist, new_year):
        # cette methode permet de mettre a jour les informations de l'oeuvre.
        self.title = new_title
        self.artist = new_artist
        self.year = new_year

    def get_age(self, current_year) :
        # Cette methode calcule et retourne l'age de l'oeuvre en fonction de l'annee actuelle.
        return current_year - self.year
        

    def is_contemporary(self, current_year, threshold):
        # cette methode determine si l'oeuvre est contemporaine en fonction d'une annee seuil.
        return self.year >= current_year - threshold 
    


       

        