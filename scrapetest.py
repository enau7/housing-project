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
    def __init__(link,prices,taxes):
        self.link = link
        self.prices = prices
        self.taxes = taxes

url = "https://www.zillow.com/browse/homes/ca/santa-barbara-county/93117/27/"
sindx1 = '"/homedetails/'
sindx2 = '"'
banned = ''
links = s.scraper(url,sindx1,sindx2,banned).scrape()
link_process(links)
print(links)

mindx1 = r'\"taxPaid\":'
mindx2 = ','
banned = ''

homes = []

for k in range(0,len(links)):
    time.sleep(2)
    history = s.scraper(links[k],mindx1,mindx2,banned).scrape()
    usd_to_int(history)
    print(history)
    homes.append(history)

print(homes)