import requests
from bs4 import BeautifulSoup
from common import __baseUrl__
import random

categories=["Category:Characters?from=Yu+Han+Sung","Category:Characters","Category:Characters?from=Kukaku+Rakukakuka"] #different endpoints for the three different character pages in the wiki


def listRandCharacter():
    '''
    This function scrapes the wiki for characters using the three character endpoints
     and stores all the characters in a list and returns a randomly chosen character
    '''


    characters=[]
    for category in categories:
        r=requests.get(f"{__baseUrl__}{category}")
        soup=BeautifulSoup(r.content,"lxml")
        for c in soup.findAll("a",class_="category-page__member-link"):
            characters.append(c.text.strip())

    return random.choice(characters)
