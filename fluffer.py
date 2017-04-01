from fluffer_helper import *
from random import randint

while true:
    links = getLinks(getRandomWord)
    link = links[randi(0, len(links) - 1)]
    visitURL(link)
