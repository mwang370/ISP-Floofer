from fluffer_helper import *
from random import randint

while True:
    try:
        links = getLinks(getSearchTerm(randint(1, 4)))
        link = links[randint(0, len(links) - 1)]
        visitURL(link)
    except:
        pass
