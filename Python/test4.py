import pymongo

client = pymongo.MongoClient("mongodb://192.168.1.72:27017/")
db = client.test
coll = db.users

query = {"name": {"$regex": "user*"}}

for value in coll.find(query):
    print(value)