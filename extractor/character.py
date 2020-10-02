import requests, re
from bs4 import BeautifulSoup
from character_list import listRandCharacter
from common import __baseUrl__, parse_characters

def getCharacterInfo():
    '''
    This function gets a random_character from listRandCharacter, parses it, sends a request,
    and scrapes the description of the character.


    '''

    info: str
    crn=listRandCharacter()
    r=requests.get(f"{__baseUrl__}{parse_characters(crn)}")
    soup=BeautifulSoup(r.content,"lxml")
    div=soup.find("div",attrs={"id":"mw-content-text"})
    allPTags=div.findAll("p")
    for x in allPTags:
        if len(list(x.text.strip()))>35: #checks if p tag has enough data to be valid
            info=x.text.strip()
            break
    return {"title":crn,"data":info}
