import requests
from bs4 import BeautifulSoup
from random import randint
import time

def goToURL(url):
	print url
	site = requests.get(url)
	content = site.content
	soup = BeautifulSoup(content)
	links = soup.find_all('a', href=True)
	
	if len(links) > 1:
		tries = 1
		link_url = links[randint(0, len(links)-1)]["href"]

		while link_url.startswith("http") == False and tries < len(links):
			link_url = links[randint(0, len(links)-1)]["href"]
			tries += 1

		time.sleep(15)
		
		try:
			goToURL(link_url)
		except:
			return

goToURL("http://github.com")

