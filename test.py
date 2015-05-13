import HTMLParser
import requests
import csv

s = requests.Session()
s.get('http://*url*/member/MbFixLogin?pToUrl=/udn/')
url="http://*url*/Searchdec2007?page=21&udndbid=udndata&SearchString=%A4%6A%B3%B0%B7%73%AE%51not%B3%B0%B0%74%2B%B3%F8%A7%4F%3D%C1%70%A6%58%B3%F8&sharepage=50&select=1&kind=2&showUserSearch=+%3Cstrong%3E%3Cfont+color%3D%23333333+class%3Dtitle03%3E%B1%7A%A5%48%3C%2Ffont%3E+%3Cfont+color%3D%23FF6600+class%3Dtitle04%3E%A4%6A%B3%B0%B7%73%AE%51not%B3%B0%B0%74%2B%B3%F8%A7%4F%3D%C1%70%A6%58%B3%F8%3C%2Ffont%3E+%3Cfont+color%3D%23333333+class%3Dtitle03%3E%A6%40%B7%6A%B4%4D%A8%EC%3C%2Ffont%3E+%3Cfont+color%3D%23FF6600+class%3Dtitle04%3E1138%3C%2Ffont%3E+%3Cfont+color%3D%23333333+class%3Dtitle03%3E%B5%A7%B8%EA%AE%C6%3C%2Ffont%3E%3C%2Fstrong%3E"
url2="http://*url*/Searchdec2007?page=22&udndbid=udndata&SearchString=%A4%6A%B3%B0%B7%73%AE%51not%B3%B0%B0%74%2B%B3%F8%A7%4F%3D%C1%70%A6%58%B3%F8&sharepage=50&select=1&kind=2&showUserSearch=+%3Cstrong%3E%3Cfont+color%3D%23333333+class%3Dtitle03%3E%B1%7A%A5%48%3C%2Ffont%3E+%3Cfont+color%3D%23FF6600+class%3Dtitle04%3E%A4%6A%B3%B0%B7%73%AE%51not%B3%B0%B0%74%2B%B3%F8%A7%4F%3D%C1%70%A6%58%B3%F8%3C%2Ffont%3E+%3Cfont+color%3D%23333333+class%3Dtitle03%3E%A6%40%B7%6A%B4%4D%A8%EC%3C%2Ffont%3E+%3Cfont+color%3D%23FF6600+class%3Dtitle04%3E1138%3C%2Ffont%3E+%3Cfont+color%3D%23333333+class%3Dtitle03%3E%B5%A7%B8%EA%AE%C6%3C%2Ffont%3E%3C%2Fstrong%3E"
url3="http://*url*/Searchdec2007?page=23&udndbid=udndata&SearchString=%A4%6A%B3%B0%B7%73%AE%51not%B3%B0%B0%74%2B%B3%F8%A7%4F%3D%C1%70%A6%58%B3%F8&sharepage=50&select=1&kind=2&showUserSearch=+%3Cstrong%3E%3Cfont+color%3D%23333333+class%3Dtitle03%3E%B1%7A%A5%48%3C%2Ffont%3E+%3Cfont+color%3D%23FF6600+class%3Dtitle04%3E%A4%6A%B3%B0%B7%73%AE%51not%B3%B0%B0%74%2B%B3%F8%A7%4F%3D%C1%70%A6%58%B3%F8%3C%2Ffont%3E+%3Cfont+color%3D%23333333+class%3Dtitle03%3E%A6%40%B7%6A%B4%4D%A8%EC%3C%2Ffont%3E+%3Cfont+color%3D%23FF6600+class%3Dtitle04%3E1138%3C%2Ffont%3E+%3Cfont+color%3D%23333333+class%3Dtitle03%3E%B5%A7%B8%EA%AE%C6%3C%2Ffont%3E%3C%2Fstrong%3E"
class parseLinks(HTMLParser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name,value in attrs:
                if name == 'href':
                    if value[0:19]=='*url*/Story2007?no':
                        print "http://*url*"+value
lParser = parseLinks()
lParser.feed(s.get(url).text)
lParser.feed(s.get(url2).text)
lParser.feed(s.get(url3).text)
lParser.close()
