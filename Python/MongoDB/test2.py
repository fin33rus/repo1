import pymongo

# подключение к серверу
client = pymongo.MongoClient("mongodb://192.168.1.72:27017/")
# выбор бд и коллекции
db = client.test
coll = db.users

# добавление пользователей
data = [
    {
        "_id": 3,
        "name": "user3"
    },
    {
        "_id": 4,
        "name": "user4"
    }
]

coll.insert_many(data)