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

    def display_info(self):
        info = self.get_info()
        for key, value in info.items():
            print(f"{key}: {value}")
       

        