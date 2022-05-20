from pymongo import MongoClient
from pprint import pprint
from collections import namedtuple
import pandas as pd


# defining organization data model
Organizations = namedtuple(
    "Organizations", 
    "admin0pcode admin0pcode_inactive organization_name organization_tag organization organization_type"
)


# connecting to mongodb and fetching all organizations from DB
client = MongoClient()
db = client.ngmReportHub
collection = db.organizations
db_organizations = collection.find()


# a set of all organizations fetched from DB
all_organizations = set()

for orgs in db_organizations:
    organizations = Organizations(orgs['admin0pcode'], orgs['admin0pcode_inactive'], orgs['organization_name'], orgs['organization_tag'], orgs['organization'], orgs['organization_type'])
    all_organizations.add(organizations)

# this dataframe contains all unique organizations from database
df = pd.DataFrame(all_organizations)