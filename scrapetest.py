import scraper as s
import time

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

class homedata:
    def __init__(latitude, longitude, taxes):
        self.latitude = latitude
        self.longitude = longitude
        self.taxes = taxes
    def to_dict():
        output = {
            "latitude" : self.latitude,
            "longitude" : self.longitude,
        }
        return output

url = "https://www.zillow.com/browse/homes/ca/santa-barbara-county/93117/27/"
sindx1 = '"/homedetails/'
sindx2 = '"'
linktails = s.scraper(url).parse(sindx1,sindx2)

mindx1 = r'\"taxPaid\":'
mindx2 = ','
homes = []

for k in range(0,len(linktails)):
    time.sleep(2)
    housescraper = s.scraper("https://www.zillow.com/homedetails/" + linktails[k])
    history = housescraper.parse(mindx1,mindx2)
    #latitude = getLat(linktails[k])
    #longitude = getLong(linktails[k])
    usd_to_int(history)
    print(history)
    print(s.getCoords(linktails[k]))
    homes.append(history)

print(homes)