import pymongo
import logging


async def add_user_to_db(user_id, unique=False):
    try:
        client = pymongo.MongoClient("mongodb://mongodb:27017/")
        db = client["users"]
        col = db["user_ids"]
        if unique:
            x = col.find_one({"user_id": user_id})
            if x:
                return
        col.insert_one({"user_id": user_id})

        total = 0
        for user in col.find():
            total += 1
        client.close()
        return str(total)
    except Exception as exc:
        return str(exc)


async def add_valentine(user_id):
    try:
        client = pymongo.MongoClient("mongodb://mongodb:27017/")
        db = client["users"]
        col = db["valentines"]
        col.insert_one({"author": user_id})
        client.close()
    except Exception:
        return -1
