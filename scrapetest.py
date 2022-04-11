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
    def __init__(lat, long, prices, taxes, ):
        self.link = link
        self
        self.prices = prices
        self.taxes = taxes

url = "https://www.zillow.com/browse/homes/ca/santa-barbara-county/93117/27/"
sindx1 = '"/homedetails/'
sindx2 = '"'
links = s.scraper(url).parse(sindx1,sindx2)
link_process(links)
print(links)

mindx1 = r'\"taxPaid\":'
mindx2 = ','
homes = []

for k in range(0,len(links)):
    time.sleep(2)
    housescraper = s.scraper(links[k])
    history = housescraper.parse(mindx1,mindx2)
    usd_to_int(history)
    print(history)
    homes.append(history)

print(homes)