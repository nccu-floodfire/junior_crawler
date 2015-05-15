# -*- coding: utf8 -*-
import HTMLParser
import requests
import csv

class parseLinks(HTMLParser.HTMLParser):
	is_a=''
	def handle_starttag(self, tag, attrs):
		if tag == 'ul':
			for name,value in attrs:
				if name == 'id':
					if value == 'newslistul':
						self.is_a=1
		elif tag == 'a' and self.is_a == 1:
			for name,value in attrs:
				if name == 'href':
					if value[0:5] == '/news':
						print "http://news.ltn.com.tw"+value
	def handle_endtag(self, tag):
		if tag == 'ul':
			self.is_a=''

text=u'陸配+中國配偶+中國新娘' #搜尋關鍵字
url='http://news.ltn.com.tw/search?keyword='+text+'&conditions=or'
lParser = parseLinks()
for syear in range(2005,2016):
	smonth=1
	while (smonth<11): #自由時報限制每次只能抓三個月，因而循環抓取1~3月、4~6月、7~9月、9~11月的搜索結果link
		emonth=smonth+2
		url1=url+'&SYear='+str(syear)+'&SMonth='+str(smonth)+'&SDay=1&EYear='+str(syear)+'&EMonth='+str(emonth)+'&EDay=1'
		html=requests.get(url1).text
		lParser.feed(html)
		lParser.close()
		smonth=smonth+3
	else: #補充抓取12月的資料
		url1=url+'&SYear='+str(syear)+'&SMonth=12&SDay=2&EYear='+str(syear)+'&EMonth=12&EDay=31'
		html=requests.get(url1).text
		lParser.feed(html)
		lParser.close()