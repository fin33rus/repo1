import pymongo
import datetime

client = pymongo.MongoClient("mongodb://192.168.1.72:27017/")
db = client.test
coll = db.users

data = {
    "_id": 5,
    "status": True,
    "time": datetime.datetime.now(),
    "flags": [1, 2 ,3]
}

coll.insert_one(data)