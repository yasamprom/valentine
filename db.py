import pymongo


async def add_user_to_db(user_id, unique=False):
    client = pymongo.MongoClient("mongodb://root:pass@127.0.0.1:27017")
    db = client["users"]
    col = db["user_ids"]
    if unique:
        x = col.find_one(user_id)
        if x:
            return
    col.insert_one({"user_id": user_id})


async def add_valentine(user_id):
    client = pymongo.MongoClient("mongodb://root:pass@127.0.0.1:27017")
    db = client["users"]
    col = db["valentines"]
    col.insert_one({"user_id": user_id})
