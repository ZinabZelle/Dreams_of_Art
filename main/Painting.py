class Painting:
    def __init__(self, title, artist, year, painting_style):
        super(). __init__(title, artist, year)
        self.painting_style = painting_style

    def get_info(self):
        artwork_info = super().get_info()   
        artwork_info["Painting Style"] = self.painting_style
        return artwork_info

class sculpture:
    def __init__ (self, title, artist, year, material, dimensions):
        super(). __init__(title, artist, year)
        self.material = material
        self.dimensions = dimensions

    def get_info(self):
        artwork_info = super().get_info()
        artwork_info["Material"] = self.material  
        artwork_info["Dimensions"] = self.dimensions
        return artwork_info 

    