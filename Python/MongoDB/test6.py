import pymongo

client = pymongo.MongoClient("mongodb://192.168.1.72:27017/")
db = client.test
coll = db.users

result = coll.count_documents({"name": {"$regex": "user*"}})
print(result)