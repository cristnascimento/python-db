from pymongo import MongoClient

client = MongoClient()
# client = MongoClient('localhost', 27017)

db = client.db_01
collection = db.persons

person = {"name" : "John", "age": 32, "city": "London"}
#collection.insert_one(person)

result = collection.find_one({"name": "John"})
print(result)

for item in collection.find({"name": "John"}):
    print(item)
