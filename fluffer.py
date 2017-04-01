from fluffer_helper import *
from random import randint

while True:
    links = getLinks(getSearchTerm(randint(1, 5)))
    link = links[randint(0, len(links) - 1)]
    visitURL(link)
