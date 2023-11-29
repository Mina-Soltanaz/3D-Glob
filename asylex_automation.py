
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import pandas as pd
import os
import json
# import geojson 

## Get environment variables
GCP_SERVICE_ACCOUNT_KEY = os.environ["GCP_SERVICE_ACCOUNT_KEY"]
SHEET_ID = os.environ["SHEET_ID"]

## SOURCE: https://medium.com/geekculture/2-easy-ways-to-read-google-sheets-data-using-python-9e7ef366c775
# Set up the credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

print(type(GCP_SERVICE_ACCOUNT_KEY))
print(GCP_SERVICE_ACCOUNT_KEY)

creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(GCP_SERVICE_ACCOUNT_KEY), scope)
client = gspread.authorize(creds)

# Open the Google Sheet using its name
# 1F3XoC8hm-AgPMALQxoXAMS-DyGfAnRtcV27ysGRS4J8 - Asylex
# 1Qt48KMf-04KXTGCyutH6cKAocKDWB5kJNSZnv-mOvjA - sample
sheet = client.open_by_key(SHEET_ID)

# # Fetch all data
# all_data = pd.DataFrame(sheet.sheet1.get_all_records())
# country_list = all_data.to_json(orient='records', lines=True).splitlines()
# country_list = [json.loads(px) for px in country_list]
# final_json = {"list" : country_list}

#Read the treaty bodies
untreatybodies = sheet.worksheet('UNTreatyBodies').get_all_records()
regionalbodies = sheet.worksheet('Regional').get_all_records()

all_bodies = { "UNTrendyBody" : untreatybodies,
              "regionalOnes" : regionalbodies}

#write to the specified json file
with open("data\\UNTrendyBodyAndRegionalOnes.json", "w+") as fp:
         json_load = json.dumps(all_bodies, indent=2)
         fp.write(json_load)
         
# Adding country_list to another json file which will be uploaded to a github repo

# # country_list =[]


# json_data = json.dumps(final_json, indent=2)

# if not os.path.exists("data"):
#     os.mkdir("data")

# with open("data/final_json.json", "w+") as json_files:
#     json_files.write(json_data)
