from sgmllib import SGMLParser
import requests
import csv
ext=''
title=''
time=''
part=''


class ListName(SGMLParser):
	is_a=""
	def start_div(self, attrs):
		for name,value in attrs:
			if name == 'class':
				if value == 'guide boxTitle':
					self.is_a=1
				elif value == 'text  boxTitle':
					self.is_a=2
	def end_div(self):
		self.is_a=""
	def start_h1(self, attrs):
		self.is_a=3
	def end_h1(self):
		self.is_a=""
	def handle_data(self, text):
		if self.is_a ==1:
			global part
			part=text
		elif self.is_a ==2:
			global ext
			ext = ext + text + '\n'
			if (text[0:3]=='201') or (text[0:3]=='200'):
				global time
				time=text
		elif self.is_a ==3:
			global title
			title = text


with open('./url.txt','r') as f:
	lParser = ListName()
	with open( './itn2.csv', 'wb') as e:
		writer = csv.writer(e)
		for line in f:
			url = line.strip('\n')
			html=requests.get(url).text
			lParser.feed(html)
			lParser.close()
			data = [(time.encode('utf8'),title.encode('utf8'),part.encode('utf8'),ext.encode('utf8'),url)]
			writer.writerows(data)
			ext=''
			time=''
			title=''
			part=''
