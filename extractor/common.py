__baseUrl__="https://towerofgod.fandom.com/wiki/"

def parse_characters(cr):
    if " " in cr:
        clist=cr.split(" ")
        x="_".join(clist)
        return x
    return cr
