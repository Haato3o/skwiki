import requests
from bs4 import BeautifulSoup
wikiUrl = 'http://wiki.spiralknights.com/'
mediaUrl = 'http://media3.spiralknights.com/wiki-'
request = requests.Session()

class item:
	'''
		Searches Spiral Knights wiki for the desired item.
	'''
	def __init__(self, name):
		'''
			:name: Item name
		'''
		self.name = name.replace(' ', '_').title()
	
	def description(self):
		'''
			Function to get item description
			:name: Item name
			:return: String
		'''
		try:
			content = request.get(wikiUrl+self.name).text
			htmlParser = BeautifulSoup(content, 'html.parser')
			htmlParser.find(alt='stats')
			description = htmlParser.find(id='Description').find_next('p').get_text()
			return description
		except Exception:
			print(Exception)
			print('No item found.')
	
	def image(self):
		'''
			Function to get item image
			:name: Item name
			:return: String
		'''
		try:
			content = request.get(wikiUrl+self.name).text
			htmlParser = BeautifulSoup(content, 'html.parser')
			htmlParser.find(alt='stats')
			image = list(str(htmlParser.find('img').get('src')))
			image.remove('/')
			return '{}{}'.format(mediaUrl, ''.join(image))
		except:
			print('No item found')
	
	def status(self):
		'''
			Function to get item status
			:name: Item name
			:return: String
		'''
		try:
			content = request.get(wikiUrl+self.name).text
			htmlParser = BeautifulSoup(content, 'html.parser')
			status = list(str(htmlParser.find(alt='stats').get('src')))
			status.remove('/')
			return '{}{}'.format(mediaUrl, ''.join(image))
		except:
			print('No item found')

	def tier(self):
		'''
			Function to get item tier
			:name: Item name
			:return: String
		'''
		try:
			content = request.get(wikiUrl+self.name).text
			htmlParser = BeautifulSoup(content, 'html.parser')
			htmlParser.find(alt='stats')
			tier = htmlParser.find('td').find_all_next('td')[3].get_text()
			return tier.strip('\n ')
		except:
			print('No item found')
