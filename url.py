import requests
from bs4 import BeautifulSoup

links = ['wiki/Tomoe_Oreki']

for link in links:
	data = requests.get('https://hyouka.fandom.com/' + link)

	soup = BeautifulSoup(data.text, 'html.parser')

	div = soup.find('table', { 'class': 'navbox mw-collapsible' })

	for ul in div.find_all('li'):
		for li in ul.find_all('a'):
			link = li.get('href')

			print('\'' + link + '\'' + ',')
