class Artwork:
    def __init__(self, title, artist, year, painting_style=None):
        self.title = title
        self.artist = artist
        self.year = year
        self.painting_style = painting_style

    def get_info(self):
        artwork_info = {
            "Title": self.title,
            "Artist": self.artist,
            "Year": self.year,
            "Painting Style": self.painting_style
        }
        return artwork_info

    


       

        