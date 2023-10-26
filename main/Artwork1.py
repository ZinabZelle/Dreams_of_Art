class Artwork:
    def __init__ ( self, title, artist, year ): # verifier
        self.title = title
        self.artist = artist
        self.year = year
        

    def get_info(self):
        return {
            "Title": self.title,
            "Artist": self.artist,
            "Year": self.year
        
        }

    def update_info(self, new_title, new_artist, new_year):
        self.title = new_title
        self.artist = new_artist
        self.year = new_year

    def get_age(self, current_year):
        return current_year - self.year

    def is_contemporary(self, current_year, threshold): #a Verifier
        return self.year >= threshold

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Year: {self.year}")
        