import pymongo
from pymongo import MongoClient

def handling_msg_missed(message):
    client = pymongo.MongoClient("<MONGODB URL>")
    db = client["<DATABASE NAME>"]
    col = db["<COLLECTION NAME>"]

    dict = { "message": message}

    insert_doc = col.insert_one(dict)

    return insert_doc.inserted_id
