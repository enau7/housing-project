import scraper as s
import pandas as pd
import time
import random

def usd_to_int(arr):
    for i in range(0,len(arr)):
        if arr[i] == 'null':
            arr[i] = None
            continue
        arr[i] = arr[i].replace("$","")
        arr[i] = arr[i].replace(",","")
        arr[i] = arr[i].replace(" ","")
        arr[i] = float(arr[i])

def link_process(arr):
    for i in range(0,len(arr)):
        arr[i] = "https://www.zillow.com/homedetails/" + arr[i]

def getCoords(address):
    url = "https://www.google.com/maps/search/"+address[0:address.find('/')]+"/"
    raw = s.scraper(url).parse("staticmap?center=","&")[0]
    latitude = float(raw[0:raw.find("%")])
    longitude = float(raw[raw.find("C")+1:raw.find("&")])
    return [latitude,longitude]

def sethomevalue(home_dict,housescraper,string):
    formatted = r'\"'+string+r'\":'
    try: 
        data = housescraper.parse(formatted,',')[0]
        try: 
            data = float(data)
        except:
            data = data.replace('"','')
            data = data.replace(chr(92),'')
    except: 
        data = None
    if data == 0:
    home_dict[string].append(data)

url = "https://www.zillow.com/browse/homes/ca/santa-barbara-county/93117/27/"
sindx1 = '"/homedetails/'
sindx2 = '"'
linktails = s.scraper(url).parse(sindx1,sindx2)

homes = {"latitude" : [],
         "longitude" : [],
         "streetAddress" : [],
         "city" : [],
         "state" : [],
         "zipcode" : [],
         "bedrooms" : [],
         "bathrooms" : [],
         "price" : []}

for k in range(0,len(linktails)):
    housescraper = s.scraper("https://www.zillow.com/homedetails/" + linktails[k])

    for i in homes.keys():
        sethomevalue(homes,housescraper,i)
    
    print(k)
    print(homes["latitude"][k])

    if k % 20 == 0:
        sleeptime = (random.random()+.5)*10
        print("sleeping for", sleeptime , "seconds")
        time.sleep(sleeptime)

df = pd.DataFrame.from_records(homes)
print(df)
df.to_csv('out.csv',index=False)