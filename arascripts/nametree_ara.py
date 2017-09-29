from pymongo import MongoClient
import json

from araontology import ARAOntology

# grab the name tree
araont = ARAOntology ( "atlases", "ara", "mongodb://localhost:27017" )
name_tree = araont.name_tree(997)

#load it into a mongo database
client = MongoClient ( )
db = client['atlases']
collection = db['ara_nametree']
collection.drop()

collection.insert(name_tree)
