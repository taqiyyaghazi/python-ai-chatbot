import pymongo
from pymongo import MongoClient

def handling_msg_missed(message):
    client = pymongo.MongoClient("mongodb+srv://taqiyyaghazi:7bgnKzVxsG77U3dT@cluster0.rovcj.mongodb.net/?retryWrites=true&w=majority")
    db = client["myportfolio-db"]
    col = db["chatbot-missed"]

    dict = { "message": message}

    insert_doc = col.insert_one(dict)

    return insert_doc.inserted_id
