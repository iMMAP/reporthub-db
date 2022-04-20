from pymongo import MongoClient
from pprint import pprint
import sqlite3
import pandas as pd
from bson.objectid import ObjectId


con = sqlite3.connect(":memory:")

con.execute("CREATE TABLE act (cluster,name,description,created_at);")

client = MongoClient()

db = client.ngmHealthCluster

collection = db.activities
#collection = db.project

sss = collection.find()

for project in sss:
    if isinstance(project['activity_type'], list):
        ats = project['activity_type']
        for at in ats:
            if isinstance(at, dict):
                con.execute("""
                INSERT INTO act VALUES (?, ?, ?, ?)
                    """, [
                        at['cluster'],
                        at['activity_type_id'],
                        at['activity_type_name'],
                        project['createdAt']
                    ])
