import scraper as s

url = "https://www.zillow.com/lompoc-ca-93117/"
sindx1 = '"list-card-price">'
sindx2 = '</div>'
banned = ''
    
subs = s.inscraper(url,sindx1,sindx2,banned).scrape()
print(subs)

for i in range(0,len(subs)):
    subs[i] = subs[i].replace("$","")
    subs[i] = subs[i].replace(",","")
    subs[i] = int(subs[i])

print(subs)
