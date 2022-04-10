import scraper as s

def usd_to_int(arr):
    for i in range(0,len(arr)):
        arr[i] = arr[i].replace("$","")
        arr[i] = arr[i].replace(",","")
        arr[i] = arr[i].replace(" ","")
        arr[i] = int(arr[i])

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
    
links = s.inscraper(url,sindx1,sindx2,banned).scrape()
link_process(links)
print(links)

mindx1 = '<span class="hdp__sc-reo5z7-1 hvBPYp">"'
mindx2 = '"'

homes = []

#for k in range(0,len(links)):
#    history = s.inscraper(links[k],mindx1,mindx2,banned).scrape()
#    usd_to_int(history)
#    homes.append(history)
#
#print(homes)