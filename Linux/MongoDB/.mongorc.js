var no = function() {
    print("Do not do this")
};

// Предотвращаем удаление баз данных;
db.dropDatabase = DB.prototype.dropDatabase = no;
// Предотвращаем удаление коллекций;
DBCollection.prototype.drop = no;
// Предотвращаем удаление индекса;
DBCollection.prototype.dropIndex = no;
// Предотвращаем удаление индексов;
DBCollection.prototype.dropIndexes = no;