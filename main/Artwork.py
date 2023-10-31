class Artwork:
    def __init__ ( self, title, artist, year ): # verifier
        self.title = title
        self.artist = artist
        self.year = year
        

    def get_info(self):
        artwork_info = {
            "Title" : self.title,
            "Artist" : self.artist,
            "Year" : self.year
        }
        return artwork_info
    
    def update_info(self, new_title, new_artist, new_year):
        self.title = new_title
        self.artist = new_artist
        self.year = new_year

    def get_age(self, current_year) :
        age = current_year - self.year
        return age

    def is_contemporary(self, current_year, threshold):
        return self.year >= (current_year - threshold)  

       

        