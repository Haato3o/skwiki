'''
Spiral Knights Wiki Parser made by Haato
                How to use
import skwiki
skwiki.item_description('item name')
returns the <item name> description

skwiki.item_status('item name')
returns the <item name> status

skwiki.item_image('item name')
returns the <item name> image

skwiki.item_tier('item name')
returns how many stars the <item name> has

if any of the functions return False, then the wiki is either offline or the item name is invalid.

'''
import urllib
import urllib.request
try:
	from bs4 import BeautifulSoup
except:
	print('BeautifulSoup required, download it before running the script.')

def item_description(ITEM_NAME: str):
		ITEM_NAME = ITEM_NAME.replace(" ", "_")
		URL = 'http://wiki.spiralknights.com/%s' % ITEM_NAME.title()
		try:
			URL = urllib.request.urlopen(URL).read()
			URL = URL.decode('utf-8')
			SOUP_HTML_PARSER = BeautifulSoup(URL, 'html.parser')
			try:
				SOUP_HTML_PARSER.find(alt='stats')
				ITEM_DESCRIPTION = SOUP_HTML_PARSER.find(id='Description')
				ITEM_DESCRIPTION = ITEM_DESCRIPTION.find_next('p')
				ITEM_DESCRIPTION = ITEM_DESCRIPTION.get_text()
				return ITEM_DESCRIPTION
			except:
				return False
		except:
			return False

def item_image(ITEM_NAME: str):
	ITEM_NAME = ITEM_NAME.replace(" ", "_")
	URL = 'http://wiki.spiralknights.com/%s' % ITEM_NAME.title()
	try:
		URL = urllib.request.urlopen(URL).read()
		URL = URL.decode('utf-8')
		SOUP_HTML_PARSER = BeautifulSoup(URL, 'html.parser')
		try:
			SOUP_HTML_PARSER.find(alt='stats')
			ITEM_IMAGE = SOUP_HTML_PARSER.find('img')
			ITEM_IMAGE = list(str(ITEM_IMAGE.get('src')))
			ITEM_IMAGE.remove('/')
			ITEM_IMAGE = "".join(ITEM_IMAGE)
			ITEM_IMAGE_URL = 'http://media.spiralknights.com/wiki-%s' % ITEM_IMAGE
			return ITEM_IMAGE_URL
		except:
			return False
	except:
		return False

def item_status(ITEM_NAME: str):
	ITEM_NAME = ITEM_NAME.replace(" ", "_")
	URL = 'http://wiki.spiralknights.com/%s' % ITEM_NAME.title()
	try:
		URL = urllib.request.urlopen(URL).read()
		URL = URL.decode('utf-8')
		SOUP_HTML_PARSER = BeautifulSoup(URL, 'html.parser')
		try:
			ITEM_STATUS = SOUP_HTML_PARSER.find(alt='stats')
			ITEM_STATUS = list(str(ITEM_STATUS.get('src')))
			ITEM_STATUS.remove('/')
			ITEM_STATUS = "".join(ITEM_STATUS)
			ITEM_STATUS_URL = 'http://media.spiralknights.com/wiki-%s' % ITEM_STATUS
			return ITEM_STATUS_URL
		except:
			return False
	except:
		return False

def item_tier(ITEM_NAME: str):
	ITEM_NAME = ITEM_NAME.replace(" ", "_")
	URL = 'http://wiki.spiralknights.com/%s' % ITEM_NAME.title()
	try:
		URL = urllib.request.urlopen(URL).read()
		URL = URL.decode('utf-8')
		SOUP_HTML_PARSER = BeautifulSoup(URL, 'html.parser')
		try:
			SOUP_HTML_PARSER.find(alt='stats')
			ITEM_TIER = SOUP_HTML_PARSER.find('td')
			ITEM_TIER = ITEM_TIER.find_all_next('td')
			ITEM_TIER = ITEM_TIER[3].get_text()
			ITEM_TIER = list(ITEM_TIER)
			ITEM_TIER.remove(ITEM_TIER[6])
			ITEM_TIER = "".join(ITEM_TIER)
			return ITEM_TIER
		except:
			return False
	except:
		return False
