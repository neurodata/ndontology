from pymongo import MongoClient

client=MongoClient()

db = client.atlases
collection = db.ara

collection.create_index("id")

