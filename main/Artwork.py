#La methode d'annulation ( method override) est utilisee ici.
#Dans la sous-classe (par exemple, Painting ou sculpture), la methode get_info de la classe de base (Artwork) est remlacee par 
#implementation specifique a la sous-classe, qui combine les informations de la classe de base et les attributs specifiques a la sous-classe
#(dans ce cas, le style de la peinture pour Painting).

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
        age = current_year - self.year
        return age

    def is_contemporary(self, current_year, threshold):
        # cette methode determine si l'oeuvre est contemporaine en fonction d'une annee seuil.
        return self.year >= (current_year - threshold)  

       

        