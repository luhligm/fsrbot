from pymongo import MongoClient

cluseter = MongoClient("mongodb+srv://fsrbot:mongofuerfsr@discord.olmby.mongodb.net/test")
db = cluseter['discord']
collection = db['fsruser']
config = db['fsrconfig']


def getConfig(arg):
    query = {"_id": {"$eq": 1}}
    data = config.find_one(query)
    return data[str(arg)]


def getUser(id):
    query = {"_id": {"$eq": id}}
    return collection.find_one(query)


def editUser(id, data, new):
    delquery = {"_id": {"$eq": int(id)}}
    newvalue = {"$set": {data: new}}
    collection.update_one(delquery, newvalue)


def alreadyExists(id):
    query = {"_id": {"$eq": int(id)}}
    return bool(collection.find_one(query))


def alreadyRegistered(id):
    query = {"_id": {"$eq": int(id)}}
    return bool(collection.find_one(query))
