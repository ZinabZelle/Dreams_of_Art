from Artwork import Artwork
from Painting import Painting
from Sculpture import sculpture
from Collection import Collection

monet = Painting(title = "Water Lilies", artist="Claude Monet", year=1916, painting_style= "Impressionism") 
picasso = Painting(title="Les Demoiselles d'Avignon", artist = "Pablo Picasso", year= 1907, painting_style="Cubism")
rodin = sculpture(title= "The Thinker", artist ="Auguste Rodin", year=1902, material="Bronze", dimensions="1.87 meters") 

my_collection = Collection(name ="My Art Collection")
my_collection.add_artwork(monet)
my_collection.add_artwork(picasso)
my_collection.add_artwork(rodin)

collection_info = my_collection.get_collection()
print("Informations sur la collection:")
print(collection_info)