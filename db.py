import json
import os

import requests


async def add_user_to_db(user_id):
    DB_TOKEN = os.getenv("DB_TOKEN")
    url = "https://data.mongodb-api.com/app/data-ghxbt/endpoint/data/beta/action/insertOne"
    data = json.dumps({
        "collection": "user_id",
        "database": "users",
        "dataSource": "mydata",
        "document": {
          "user_id": user_id
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': DB_TOKEN
    }
    requests.request("POST", url, headers=headers, data=data)



