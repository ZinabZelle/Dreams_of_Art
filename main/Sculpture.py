from Artwork import Artwork

class sculpture(Artwork):
    def __init__ (self, title, artist, year, material, dimensions):
        super(). __init__(title, artist, year)
        self.material = material
        self.dimensions = dimensions