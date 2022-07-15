import pymongo

client = pymongo.MongoClient("mongodb://192.168.1.72:27017/")
db = client.test
coll = db.users

for value in coll.find().sort("name", -1):
    print(value)