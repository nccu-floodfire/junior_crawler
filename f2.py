from sgmllib import SGMLParser
import requests
import csv
ext=''
title=''
time=''
part=''


class ListName(SGMLParser):
	is_a=""
	def start_span(self, attrs):
		for name,value in attrs:
			if name == 'class':
				if value == 'story_title':
					self.is_a=2
	def end_span(self):
		self.is_a=""
	def start_p(self, attrs):
		self.is_a=1
	def end_p(self):
		self.is_a=""
	def start_td(self, attrs):
		self.is_a=1
	def end_td(self):
		self.is_a=""
	def handle_data(self, text):
		if self.is_a:
			global ext
			ext = ext + text
			if (text[1:4]=='201') or (text[1:4]=='200') or (text[1:4]=='199') or (text[1:4]=='198'):
				global time
				global part
				time=text[1:11]
				part=text[16:]
			if text[1:4]=='200':
				time=text[1:11]
				part=text[16:]
			elif self.is_a ==2:
				global title
				title = text

with open('./url.txt','r') as f:
	lParser = ListName()
	s = requests.Session()
	s.get('http://*url*/member/MbFixLogin?220243238')
	with open( './data8.csv', 'wb') as e:
		writer = csv.writer(e)
		for line in f:
			url = line.strip('\n')
			url = url.encode('big5')
			lParser.feed(s.get(url).text)
			lParser.close()
			data = [(time.encode('big5'),title.encode('big5'),part.encode('big5'),ext.encode('big5'))]
			writer.writerows(data)
			ext=''
			time=''
			title=''
			theme=''
			part=''
