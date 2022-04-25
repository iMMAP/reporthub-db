from pymongo import MongoClient
from pprint import pprint
from collections import namedtuple
import pandas as pd


# defining activity data model
Activity = namedtuple(
    "Activity", 
    "cluster activity_type_id activity_type_name"
)


# connecting to mongodb and fetching all activities from DB
client = MongoClient()
db = client.ngmHealthCluster
collection = db.activities
db_activities = collection.find()


# a set of all activities fetched from DB
all_activities = set()

for ac in db_activities:
    activity = Activity(ac['cluster'], ac['activity_type_id'], ac['activity_type_name'])
    all_activities.add(activity)

# this dataframe contains all unique activities from database
df = pd.DataFrame(all_activities)
