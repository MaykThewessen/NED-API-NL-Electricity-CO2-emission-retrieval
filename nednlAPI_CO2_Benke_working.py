import json, requests, time
from datetime import date, timedelta
import pandas as pd

# Load environment variables from .env file
import os
os.system('clear')
from dotenv import load_dotenv
load_dotenv()
NED_API_KEY = os.getenv("NED_API_KEY")


start_date  = date(2024, 1, 1)
end_date    = date(2024, 12, 31)
daysstep    = 6                 # De API kan om een of andere reden maar 144 datapunten per keer exporteren, max 6 dagen in uurwaardes, of 1 dag in kwartier of 10 minuten waardes.

exportname = 'data_export_NED_CO2_' + start_date.strftime("%Y%m%d") + '_to_' + end_date.strftime("%Y%m%d") + '_15min.xlsx'

def daterange(start_date, end_date):
    for n in range(0,int((end_date - start_date).days),daysstep):
        yield start_date + timedelta(n)

url = "https://api.ned.nl/v1/utilizations"
df1 = pd.DataFrame(columns=['capacity', 'volume', 'percentage','emission','emissionfactor','validfrom']) #initialise dataframe # ,'validto','lastupdate'

for requestdate in daterange(start_date, end_date):
    print(requestdate.strftime("%Y-%m-%d"))
    requestdate_to = requestdate + timedelta(daysstep)
    headers = {
    'X-AUTH-TOKEN': NED_API_KEY,
    'accept': 'application/ld+json'}
    
    params = {'point': 0, 
              'type': 27, 
              'granularity': 4,  # 4 = 15min, 5 = 1 hour, 6 = 1 day, 7 = 1 month, 8 = 1 year
              'granularitytimezone': 1, 
              'classification': 2, 
              'activity': 1,
              'validfrom[after]': requestdate.strftime("%Y-%m-%d"),
              'validfrom[strictly_before]': requestdate_to.strftime("%Y-%m-%d")}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False).json()

    df = pd.json_normalize(response, "hydra:member")

    df = df.drop(columns=['@id','@type','id','point','type','granularity','granularitytimezone','activity','classification','validto','lastupdate'])
    if df1.empty:
        df1 = df
    else:
        df1 = pd.concat([df1,df], ignore_index=True)

    time.sleep(0.1) # pauze om niet de API te overbevragen

# print(json.dumps(response, separators=(",",":"), indent=4))

df1.to_excel(exportname, index=False)
print(f"Data exported to {exportname}")
