import pymongo
import logging


async def add_user_to_db(user_id, unique=False):
    client = pymongo.MongoClient("mongodb://mongodb:27017/")
    db = client["users"]
    col = db["user_ids"]
    if unique:
        x = col.find_one(user_id)
        if x:
            return
    col.insert_one({"user_id": user_id})


async def add_valentine(user_id):
    client = pymongo.MongoClient("mongodb://mongodb:27017/")
    db = client["users"]
    col = db["valentines"]
    col.insert_one({"author": user_id})
