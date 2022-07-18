import pymongo

client = pymongo.MongoClient("mongodb://192.168.1.72:27017/")
db = client.test
coll = db.users

result = db.list_collection_names()
print(result)