
from main.Artwork import Artwork

class Sculpture(Artwork):
    def __init__(self, title, artist, year_created, sculpture_material):
        super().__init__(title, artist, year_created)
        self.sculpture_material = sculpture_material

    def get_info(self):
        artwork_info = super().get_info()
        artwork_info["Sculpture Material"] = self.sculpture_material
        return artwork_info



    
