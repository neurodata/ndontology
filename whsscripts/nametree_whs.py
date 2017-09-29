from pymongo import MongoClient
import json

from ndontology import NDOntology

# grab the name tree
ndont = NDOntology ( "atlases", "whs", "mongodb://localhost:27017" )
name_tree = ndont.name_tree(99999)

#load it into a mongo database
client = MongoClient ( )
db = client['atlases']
collection = db['whs_nametree']
collection.drop()

collection.insert(name_tree)
