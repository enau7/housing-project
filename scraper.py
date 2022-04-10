from urllib.request import Request, urlopen
import zlib

class exscraper:

    def __init__(self,urlA,subs,urlB,indexstart,indexend):
        self.urlA = urlA
        self.subs = subs
        self.urlB = urlB
        self.indexstart = indexstart
        self.indexend = indexend

    def webtext(self):
        req_headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.8',
            'accept-encoding' : 'gzip, deflate, br',
            'connection' : 'keep-alive',
            'referer' : 'https://www.google.com',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
        }
        req = Request(self.url, headers=req_headers)
        try:
            page = urlopen(req)
        except:
            return(None)
        html_bytes = page.read()
        try:
            html_bytes = zlib.decompress(html_bytes, 16+zlib.MAX_WBITS)
        except: pass
        html = html_bytes.decode("utf-8")
        return(html)
    
    def getdata(self,sub):
        text = self.webtext(self.urlA+sub+self.urlB)
        index = text.find(self.indexstart)+len(self.indexstart)
        text = text[index:len(text)]
        index = text.find(self.indexend)
        return(text[0:index])

    def scrape(self):
        pricedict = {}
        for k in self.subs:
            site = (self.urlA+k+self.urlB)
            try:
                pricedict[k] = self.getdata(k)
            except:
                print("Error fetching data for "+k)
        return pricedict
    
class inscraper:

    def __init__(self,url,indexstart,indexend,banned):
        self.url = url
        self.indexstart = indexstart
        self.indexend = indexend
        self.banned = banned

    def webtext(self):
        req_headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.8',
            'accept-encoding' : 'gzip, deflate, br',
            'connection' : 'keep-alive',
            'referer' : 'https://www.google.com',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
        }
        req = Request(self.url, headers=req_headers)
        try:
            page = urlopen(req)
        except:
            return(None)
        html_bytes = page.read()
        try:
            html_bytes = zlib.decompress(html_bytes, 16+zlib.MAX_WBITS)
        except: pass
        html = html_bytes.decode("utf-8")
        return(html)

    def scrape(self):
        text = self.webtext()
        if text is None:
            return(None)
        data = []
        index = 0
        blocked = 0
        while (index != -1):
            index = text.find(self.indexstart)
            if index == -1:
                break
            text = text[index+len(self.indexstart):len(text)]
            index = text.find(self.indexend)
            word = text[0:(index)]
            for k in self.banned:
                    if k in word:
                        blocked = 1
            if blocked:
                    text = text[len(word)+1:len(text)]
            else:
                data.append(word)
        return(data)