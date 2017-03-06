#Request to get population data for cities based on the city data gathered
import argparse
import requests
import os
import json
parser = argparse.ArgumentParser()
parser.add_argument("--city", dest="City", help="Enter a city name",
                    type=str)
args = parser.parse_args()
cityname=args.City
populationdata=[]
print(args.City)
h={
    'X-FullContact-APIKey': '67d9b059fd8d95ae'
    }

populationdata.append(requests.get('http://api.fullcontact.com/v2/address/locationEnrichment.json?place='+cityname,headers=h).json())
populationdirectory='Population Data'
if not os.path.exists(populationdirectory):
        os.makedirs(populationdirectory)
        with open(populationdirectory+'\\'+str(populationdata[0]['locations'][0]['country']['code'])+'.json', 'w') as outfile:
                json.dump(populationdata[0]['locations'][0], outfile)
                print("Json dumped in folder")
else:
     print("This program is just intended to understand how to get one city data. Delete populationdirectory folder and try again")



    
    
