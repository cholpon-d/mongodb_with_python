import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://admin:{password}@cluster.lq9yzqg.mongodb.net/?retryWrites=true&w=majority"
cluster = MongoClient(connection_string)

collection = cluster.shop.bikes

pattern = {
    "brand": "Fieldoo",
    "type": "Road bike",
    "price": 399,
    "color": ["Black", "White", "Red"],
    "weight": "120kg",
}

# insert first documents
# collection.insert_one(pattern)


# insert many documents
def create_documents():
    brands = ["Mongoose", "Socool", "Schwin"]
    types = ["Road bike", "Mountain bike", "Flat Road Bike"]
    prices = [480, 420, 450]
    colors = ["Black & Red", "Blue", "Orange & Black"]
    weights = ["115kg", "120kg", "120kg"]

    docs = []

    for brand, type, price, color, weight in zip(
        brands, types, prices, colors, weights
    ):
        doc = {
            "brand": brand,
            "type": type,
            "price": price,
            "color": color,
            "weight": weight,
        }
        docs.append(doc)

    collection.insert_many(docs)


# create_documents()

# show all documents
# for value in collection.find():
#     print(value)

# search by brand without _id
# query = {"brand": "Mongoose"}
# for value in collection.find(query, {"_id": 0}):
#     print(value)

# sort
# for value in collection.find().sort("price"):
#     print(value)

# find price less than 460$
# data = collection.find({"price": {"$lt": 460}})
# print(*[d["brand"] for d in data])

# update
# collection.update_one({"brand": "Fieldoo"}, {"$push": {"color": "Blue"}})
# collection.update_one({"brand": "Schwin"}, {"$inc": {"price": -80}})
# collection.update_one({"brand": "Fieldoo"}, {"$pull": {"color": "Red"}})
# collection.update_many({}, {"$set": {"metal": "aluminium"}})

# count of documents
# number = collection.count_documents({})
# print(number)

# delete
# collection.delete_one({"_id":"65c34d23fd2c208e5d9b899f"})

# delete all collections
# collection.delete_many({})
