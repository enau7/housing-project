from urllib.request import Request, urlopen
import zlib
    
class scraper:

    def __init__(self,url):
        self.url = url
        self.htmltext = None

    def webtext(self):
        if self.htmltext != None:
            return self.htmltext
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
        self.htmltext = html_bytes.decode("utf-8")
        return(self.htmltext)

    def parse(self,indexstart,indexend,banned=""):
        text = self.webtext()
        if text is None:
            return(None)
        data = []
        index = 0
        blocked = 0
        while (index != -1):
            index = text.find(indexstart)
            if index == -1:
                break
            text = text[index+len(indexstart):len(text)]
            index = text.find(indexend)
            if index == -1:
                break
            word = text[0:(index)]
            for k in banned:
                    if k in word:
                        blocked = 1
            if blocked:
                pass #text = text[len(word)+1:len(text)]
            else:
                data.append(word)
        return(data)