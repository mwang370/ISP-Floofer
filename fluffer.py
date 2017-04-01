from fluffer_helper import *
from random import randint

while True:
    links = getLinks(getRandomWord())
    link = links[randint(0, len(links) - 1)]
    visitURL(link)
