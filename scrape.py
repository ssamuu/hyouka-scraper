import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv() 

mongo = os.getenv('MONGO_URI')
client = MongoClient(mongo)

links = ['/wiki/Houtarou_Oreki', '/wiki/Eru_Chitanda', '/wiki/Satoshi_Fukube', '/wiki/Mayaka_Ibara', '/wiki/Tomoe_Oreki', '/wiki/Ayako_Kouchi', '/wiki/Fuyumi_Irisu', '/wiki/Jirou_Tanabe', '/wiki/Junya_Nakajou', '/wiki/Kaho_Juumonji', '/wiki/Koreyuki_Tani', '/wiki/Kurako_Eba', '/wiki/Masashi_Toogaito', '/wiki/Mayu_Hongou', '/wiki/Misaki_Sawakiguchi', '/wiki/Muneyoshi_Kugayama', '/wiki/Shouko_Yuasa', '/wiki/Tomohiro_Haba', '/wiki/Yasukuni_Yoshino', '/wiki/Jun_Sekitani', '/wiki/Haruna_Anjou', '/wiki/Kayo_Zenna', '/wiki/Masakiyo_Ogi', '/wiki/Omichi', '/wiki/Rie_Zenna', '/wiki/Youko_Itoigawa']

#links = ['/wiki/Houtarou_Oreki', '/wiki/Eru_Chitanda', '/wiki/Satoshi_Fukube', '/wiki/Mayaka_Ibara']
character =[]

for link in links:
	try:
		person = {}
		data = requests.get('https://hyouka.fandom.com' + link)

		soup = BeautifulSoup(data.text, 'html.parser')

		div = soup.find('aside', { 'role': 'region' })

		name = div.find('h2', {'data-source':'name'})
		ename = name.text

		image = div.find('figure', {'data-source':'image'})
		for img in image.find_all('a'):
			imgLink = img.get('href')

		text = div.find('div', {'data-source':'kanji'})
		for data in text.find_all('div', {'class':'pi-data-value pi-font'}):
			kanji = data.text

		text = div.find('div', {'data-source':'age'})
		for data in text.find_all('div', {'class':'pi-data-value pi-font'}):
			age = data.text

		text = div.find('div', {'data-source':'height'})
		for data in text.find_all('div', {'class':'pi-data-value pi-font'}):
			height = data.text

		text = div.find('div', {'data-source':'gender'})
		for data in text.find_all('div', {'class':'pi-data-value pi-font'}):
			gender = data.text

		text = div.find('div', {'data-source':'occupation'})
		for data in text.find_all('div', {'class':'pi-data-value pi-font'}):
			occupation = data.text

		text = div.find('div', {'data-source':'class'})
		for data in text.find_all('div', {'class':'pi-data-value pi-font'}):
			studentClass = data.text


	except:
		pass

		person['name'] = ename 
		person['kanji'] = kanji
		person['gender'] = gender
		person['age'] = age
		person['height'] = height
		person['occupation'] = occupation
		person['class'] = studentClass
		person['image'] = imgLink

		character.append(person)

print(character)


	# except:
	# 	pass

db = client.hyouka

for cast in character:
	db.characters.insert_one(cast)
