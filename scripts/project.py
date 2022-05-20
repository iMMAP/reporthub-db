from pymongo import MongoClient
from pprint import pprint
from collections import namedtuple
import pandas as pd


# attribute
project_attr = [
    "adminRpcode",
    "adminRname",
    "admin0pcode",
    "admin0name",
    "organization_id",
    "organization_tag",
    "organization",
    "organization_name",
    "implementing_partners_checked",
    "programme_partners_checked",
    "cluster_id",
    "cluster",
    "name",
    "position",
    "phone",
    "email",
    "username",
    "location_groups_check",
    "location_grouping_by",
    "project_acbar_partner",
    "project_hrp_project",
    "project_hrp_code",
    "project_status",
    "project_title",
    "project_description",
    "project_start_date",
    "project_end_date",
    "project_budget",
    "project_budget_currency",
    "mpc_purpose_cluster_id",
    "mpc_purpose_type_id",
    "mpc_purpose_type_name",
    "project_gender_marker",
    "private",
    "project_code",
    "project_type_other",
    "project_donor_other",
    "activity_description_other",
    "report_type_id"
]

# defining project data model
Project = namedtuple(
    "Project", 
    project_attr
)


# connecting to mongodb and fetching all project from DB
client = MongoClient()
db = client.ngmHealthCluster
collection = db.project
db_project = collection.find()

# a set of all project fetched from DB
all_project = set()

for prjct in db_project:
    
    project = Project(
    prjct["adminRpcode"],
    prjct["adminRname"],
    prjct["admin0pcode"],
    prjct["admin0name"],
    prjct["organization_id"],
    prjct["organization_tag"],
    prjct["organization"],
    prjct["organization_name"],
    prjct["implementing_partners_checked"] if ("implementing_partners_checked" in prjct.keys())  else False,
    prjct["programme_partners_checked"] if ("programme_partners_checked" in prjct.keys())  else False,
    prjct["cluster_id"],
    prjct["cluster"],
    prjct["name"],
    prjct["position"],
    prjct["phone"],
    prjct["email"],
    prjct["username"],
    prjct["location_groups_check"] if ("location_groups_check" in prjct.keys())  else False,
    prjct["location_grouping_by"] if ("location_grouping_by" in prjct.keys())  else "",
    prjct["project_acbar_partner"] if ("project_acbar_partner" in prjct.keys())  else False,
    prjct["project_hrp_project"] if ("project_hrp_project" in prjct.keys())  else False,
    prjct["project_hrp_code"] if ("project_hrp_code" in prjct.keys())  else "",
    prjct["project_status"],
    prjct["project_title"],
    prjct["project_description"],
    prjct["project_start_date"],
    prjct["project_end_date"],
    prjct["project_budget"],
    prjct["project_budget_currency"],
    prjct["mpc_purpose_cluster_id"] if ("mpc_purpose_cluster_id" in prjct.keys())  else "",
    prjct["mpc_purpose_type_id"] if ("mpc_purpose_type_id" in prjct.keys())  else "",
    prjct["mpc_purpose_type_name"] if ("mpc_purpose_type_name" in prjct.keys())  else "",
    prjct["project_gender_marker"] if ("project_gender_marker" in prjct.keys())  else "",
    prjct["private"]if ("private" in prjct.keys())  else False,
    prjct["project_code"] if ("project_code" in prjct.keys())  else "",
    prjct["project_type_other"] if ("project_type_other" in prjct.keys())  else "",
    prjct["project_donor_other"] if ("project_donor_other" in prjct.keys())  else "",
    prjct["activity_description_other"] if ("activity_description_other" in prjct.keys())  else "",
    prjct["report_type_id"] if ("report_type_id" in prjct.keys())  else "monthly"
    )
    
    all_project.add(project)
        

# this dataframe contains all unique project from database
df = pd.DataFrame(all_project)