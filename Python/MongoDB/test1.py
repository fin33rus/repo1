import pymongo

# подключение к серверу
client = pymongo.MongoClient("mongodb://192.168.1.72:27017/")
# выбор бд и коллекции
db = client.test
coll = db.users

# добавление пользователей
coll.insert_one({"_id": 1, "name": "user1"})
coll.insert_one({"_id": 2, "name": "user2"})