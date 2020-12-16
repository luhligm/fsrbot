from pymongo import MongoClient

#Config
cluseter = MongoClient("mongodb+srv://fsrbot:mongofuerfsr@discord.olmby.mongodb.net/test")
db = cluseter['discord']
collection = db['fsruser']
config = db['fsrconfig']

# bekommt Configdaten aus der Datenbank
# def getConfig(arg):
#     query = {"_id": {"$eq": 1}}
#     data = config.find_one(query)
#     return data[str(arg)]
#
# # Userabfrage aus der Datenbank anhand der ID
# def getUser(id):
#     query = {"_id": {"$eq": id}}
#     return collection.find_one(query)
#
# def addUser(userData):
#     collection.insert_one(userData)
#
#
# def editUser(id, data, new):
#     delquery = {"_id": {"$eq": int(id)}}
#     newvalue = {"$set": {data: new}}
#     collection.update_one(delquery, newvalue)
#
# # Überprüft, ob User mit der ID einen Datenbankeintrag hat
# def alreadyExists(id):
#     query = {"_id": {"$eq": int(id)}}
#     return bool(collection.find_one(query))
#
# # redundant mit alreadyExists(id)?
# def alreadyRegistered(id):
#     query = {"_id": {"$eq": int(id)}}
#     return bool(collection.find_one(query))
