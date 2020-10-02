import requests, re
from bs4 import BeautifulSoup
from character_list import listRandCharacter

def getCharacterInfo():
    info: str
    r=requests.get(f"https://towerofgod.fandom.com/wiki/{listRandCharacter()}")
    soup=BeautifulSoup(r.content,"lxml")
    div=soup.find("div",attrs={"id":"mw-content-text"})
    allPTags=div.findAll("p")
    for x in allPTags:
        if len(list(x.text.strip()))>35:
            info=x.text.strip()
            break
    return info
