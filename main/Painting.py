from Artwork import Artwork

class Painting(Artwork):
    def __init__(self, title, artist, year, painting_style):
        super().__init__(title, artist, year)
        self.painting_style = painting_style

    def get_info(self):
        artwork_info = super().get_info()
        artwork_info["Painting Style"] = self.painting_style
        return artwork_info
    



   




 

    