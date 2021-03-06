import requests
from bs4 import BeautifulSoup
from random import randint
import time

def getRandomWord():
    r = requests.get('http://www.setgetgo.com/randomword/get.php')
    return r.text

def getSearchTerm(numWords):
    searchTerm = ''
    for index in range(numWords):
        searchTerm = searchTerm + ' ' + getRandomWord()
    return searchTerm.strip()

def getLinks(searchTerm):
    headers = {'Ocp-Apim-Subscription-Key': '590188e973f14a9388649c11d27718bf'}
    params = {'q': searchTerm}
    r = requests.get('https://api.cognitive.microsoft.com/bing/v5.0/search?q=' + searchTerm + '&count=10', headers=headers, params=params)
    results = r.json()
    results = results['webPages']['value']
    links = []
    for result in results:
        links.append(result['displayUrl'])
    return links

def visitURL(url):
    try:
        site = requests.get(url)
    except:
        return
    print 'visiting: ' + url
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
                visitURL(link_url)
        except:
            return
