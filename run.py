import requests
from bs4 import BeautifulSoup
from random import randint
import time

def getRandomWord():
    r = requests.get('http://www.setgetgo.com/randomword/get.php')
    return r.text

def getLinks(word):
    headers = {'Ocp-Apim-Subscription-Key': 'a43582571a4946d0a3e7afb34d09807d'}
    params = {'q': word}
    r = requests.get('https://api.cognitive.microsoft.com/bing/v5.0/search?q=' + word + '&count=10', headers=headers, params=params)
    results = r.json()
    results = results['webPages']['value']
    links = []
    for result in results:
        links.append(result['displayUrl'])
    return links

def goToURL(url):
	print url
	site = requests.get(url)
	content = site.content
	soup = BeautifulSoup(content)
	links = soup.find_all('a', href=True)
	if len(links) > 1:
		tries = 1
		link_url = links[randint(0, len(links) - 1)]["href"]
		while link_url.startswith("http") == False and tries < len(links):
			link_url = links[randint(0, len(links) - 1)]["href"]
			tries += 1
		time.sleep(randint(15, 30))
		try:
            randi = randint(0, 3)
            if randi == 0:
                return
            else:
			    goToURL(link_url)
		except:
			return
