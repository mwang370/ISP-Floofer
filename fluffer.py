from fluffer_helper import *
from random import randint

while True:
    try:
        searchTerm = getSearchTerm(1)
        print 'searching: ' + searchTerm
        links = getLinks(searchTerm)
        link = links[randint(0, len(links) - 1)]
        visitURL(link)
    except:
        pass
