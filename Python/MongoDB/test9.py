import pymongo

client = pymongo.MongoClient("mongodb://192.168.1.72:27017/")
db = client.test
coll = db.users

current = {"username": "user3"}
new_name = {"$set": {"username": "user3-new"}}

coll.update_one(current, new_name)
