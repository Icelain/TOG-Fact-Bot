from common import __baseUrl__, parse_characters
import requests
from bs4 import BeautifulSoup
import random

def getShinsuTechnique():
    '''
    This function scrapes a random shinsu technique from the wiki
    '''

    shinsu_techniques=[]

    r=requests.get(f"{__baseUrl__}Category:Shinsu_Techniques")
    soup=BeautifulSoup(r.content, "lxml")
    for stn in soup.findAll("a",class_="category-page__member-link"):

        if not stn.text.strip().startswith("Category"):
            shinsu_techniques.append(stn.text.strip())

    return random.choice(shinsu_techniques)

def getStnInfo():
    '''
    This function scrapes data about the randomly generated shinsu technique.

    '''
    stn=getShinsuTechnique()
    info: str
    r=requests.get(f"{__baseUrl__}{parse_characters(stn)}") #parse_characters() makes the endpoints readable
    soup=BeautifulSoup(r.content, "lxml")
    div=soup.find("div",attrs={"id":"mw-content-text"})
    allPTags=div.findAll("p")
    for x in allPTags:
        if len(list(x.text.strip()))>35:
            info=x.text.strip()
            break
    return {"title":stn,"data":info} #returns a dictionary containing the title and information
