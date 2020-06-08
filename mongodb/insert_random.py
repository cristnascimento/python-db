import random
from pymongo import MongoClient

users_size = 100
activity_range = 30
weight_range = 30



client = MongoClient()
# client = MongoClient('localhost', 27017)

db = client.db_test_bk
collection = db.persons


for user in range(0, users_size):
    activity_list = []
    for day in range(0, activity_range):
        weight = random.randrange(weight_range)
        activity_list.append(weight)
    person = {"person": user, "sessions": activity_list}
    collection.insert_one(person)
