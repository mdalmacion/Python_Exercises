import requests 
import json
from bs4 import BeautifulSoup

RSS_URL = 'https://www.reddit.com/r/philippines.rss'
SUBREDDIT = 'r/philippines'
def Scrape_RSS(RSS_URL):
	article_list = []
	print('Started scraping...')
	try:
		r = requests.get(RSS_URL)
		if (r.status_code != 200):
			print(f'Cannot establish connection to: {SUBREDDIT}')
			return
		soup = BeautifulSoup(r.content, features='xml')
		
		print(soup)
		
		articles = soup.findAll('entry')
		for post in articles:
			title = post.find('title').text
			link = post.find('uri').text
			published = post.find('published').text

			article = {
				'title': title,
				'link': link,
				'published': published
			}
			article_list.append(article)

		print('Finished scraping.')
		return article_list	
	except Exception as e:
		print(f'Failed to establish connection: {e}')

def Save_RSS(article_list):
	with open('articles.txt', 'w') as outfile:
		json.dump(article_list, outfile)



Save_RSS(Scrape_RSS(RSS_URL))
