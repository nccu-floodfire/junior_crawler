from sgmllib import SGMLParser
import requests
import csv
ext=''
title=''
time=''
part=''

class ListName(SGMLParser):
	is_a=""
	is_b=''
	divnum=0
	chosendiv=''
	def start_div(self, attrs):
		self.divnum+=1
		for name,value in attrs:
			if name == 'class':
				if value == 'guide boxTitle':
					self.is_a=1
					self.chosendiv=self.divnum
				elif value == 'text  boxTitle' or value =='cont' or value =='writer' or value =='news_content':
					self.is_a=2
					self.chosendiv=self.divnum
				elif value=='Btitle':
					self.is_b=1
	def end_div(self):
		if self.divnum==self.chosendiv:
			self.is_a=''
			self.chosendiv=''
		self.divnum-=1
	def start_h1(self, attrs):
		self.is_b=1
	def end_h1(self):
		self.is_b=""
	def start_script(self,attrs):
		self.is_a=''
	def end_script(self):
		if self.divnum==self.chosendiv:
			self.is_a=2
	def handle_data(self, text):
		if self.is_a ==1:
			global part
			part=text
		elif self.is_a ==2:
			global ext
			ext = ext + text + '\n'
			ext=ext.replace('  ','')
			ext=ext.replace(' \n','')
			ext=ext.replace('\n\n','\n')
			if (text[0:3]=='201') or (text[0:3]=='200'):
				global time
				time=text
		if self.is_b:
			global title
			title=text
			self.is_b=''


with open('./url2.txt','r') as f:
	lParser = ListName()
	with open( './itn.csv', 'wb') as e:
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
