import scraper as s
import pandas as pd
import time
import random

def appendhome(home_dict,housescraper,string):
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
    if data == 0 or data == "null":
        data = None
    home_dict[string].append(data)

# The following gets all of the link "tails" to be scraped from:

url = "https://www.zillow.com/browse/homes/ca/santa-barbara-county/93117/"
sindx1 = '"/homedetails/'
sindx2 = '"'

linktails = set()

for k in range(22,29):
    linktails.update(s.scraper(url + str(k) + "/").parse(sindx1,sindx2))

# Filters out the links which are not on streets in Isla Vista:

streets = ["Del-Playa",
           "Sabado-Tarde",
           "Trigo",
           "Pasado",
           "Fortuna",
           "Sueno",
           "Estero",
           "Abrego",
           "Picasso",
           "Berkshire-Terrace",
           "Seville",
           "Madrid",
           "Pardall",
           "Cordoba",
           "Segovia",
           "El-Greco",
           "Cervantes",
           "El-Nido",
           "Camino-Majorca",
           "Camino-Lindo",
           "Camino-Corto",
           "Camino-Del-Sur",
           "Camino-Pescadero",
           "Embarcadero"]

killlist = []

for k in linktails:
    find = False
    for n in streets:
        if k.find(n) != -1:
            find = True
            break
    if find == False:
        killlist.append(k)

for k in killlist:
    linktails.remove(k)

# All of the parameters to be stored in homes:
# Stored as a dictionary because they can be converted to dataframes easily

homes = {"latitude" : [],
         "longitude" : [],
         "streetAddress" : [],
         "city" : [],
         "state" : [],
         "zipcode" : [],
         "bedrooms" : [],
         "bathrooms" : [],
         "price" : []}

linktailslist = list(linktails)

# It is easiest this way to convert to a list - we do not want repeat values 
# but we also want to iterate over it like a list, because we want to print 
# k and the latitude at position k

for k in range(0,len(linktailslist)):
    housescraper = s.scraper("https://www.zillow.com/homedetails/" + linktailslist[k])

    for i in homes.keys():
        appendhome(homes,housescraper,i)
    
    print(k)
    print(homes["latitude"][k])

    # As to not overload zillow and it kick us out, we give it a break every 20 calls:
    if (k + 1) % 20 == 0:
        sleeptime = (random.random()+.5)*10
        print("sleeping for", sleeptime , "seconds")
        time.sleep(sleeptime)

df = pd.DataFrame.from_records(homes)
print(df)
df.to_csv('out.csv',index=False)