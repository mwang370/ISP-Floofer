import requests

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
