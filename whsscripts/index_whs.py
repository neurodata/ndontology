from pymongo import MongoClient

client=MongoClient()

db = client.atlases
collection = db.whs

collection.create_index("id")
