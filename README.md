# hyouka-scraper
python script that would scrape hyouka wiki fandom then insert it in a mongodb

## Installation
```
pip install -r requirements.txt 
```
## Environment Variables
Create a ```.env``` file. Then copy this format. Replace ```YOUR_MONGO_URI``` with your mongo uri string.
```
MONGO_URI="YOUR_MONGO_URI" 
```
## Usage
```
python scrape.py 
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
