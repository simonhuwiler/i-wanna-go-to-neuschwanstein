# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Main

# %%
import requests
import json
from bs4 import BeautifulSoup
import os
from dotenv import dotenv_values


# %%
config = dotenv_values("../.env")
CASTLES = {
    'Neuschwanstein': {
        'name': 'Neuschwanstein',
        'nPoolNr': 30,
        'nTicketTypeNr': 44,
        "PersonSelection":[{"nPersonTypeNr":"1","nCount":"1"},{"nPersonTypeNr":"3","nCount":"0"},{"nPersonTypeNr":"15","nCount":"0"},{"nPersonTypeNr":"16","nCount":"0"},{"nPersonTypeNr":"17","nCount":"0"},{"nPersonTypeNr":"19","nCount":"0"},{"nPersonTypeNr":"30","nCount":"0"},{"nPersonTypeNr":"31","nCount":"0"},{"nPersonTypeNr":"32","nCount":"0"},{"nPersonTypeNr":"63","nCount":"0"},{"nPersonTypeNr":"2","nCount":"0"}]
     },
    'Hohenschwangnau':
    {
        'name': 'Hohenschwangnau',
        'nPoolNr': 24,
        'nTicketTypeNr': 41,
        "PersonSelection": [{"nPersonTypeNr":"29","nCount":"1"},{"nPersonTypeNr":"33","nCount":"0"},{"nPersonTypeNr":"34","nCount":"0"},{"nPersonTypeNr":"63","nCount":"0"}],
    }
}


# %%
def check_for_free_tickets(dtSelectedDate, castle):
    print("%s - %s" % (castle['name'], dtSelectedDate))
    params = {
        #"PersonSelection": [{"nPersonTypeNr":"29","nCount":"1"},{"nPersonTypeNr":"33","nCount":"0"},{"nPersonTypeNr":"34","nCount":"0"},{"nPersonTypeNr":"63","nCount":"0"}],
        "PersonSelection": castle['PersonSelection'],
        'electedSubContigents': [],
        'bReservation': "true",
        'dtSelectedDate': "%s" % dtSelectedDate,
        'dtStartDate': "%s" % dtSelectedDate,
        'nDays': 0,
        'nPlaces': 2,
        'nPoolNr': "%s" % castle['nPoolNr'],
        'nTicketTypeNr': "%s" % castle['nTicketTypeNr']
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'Host': 'shop.ticket-center-hohenschwangau.de',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json',
        'Origin': 'https://shop.ticket-center-hohenschwangau.de',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://shop.ticket-center-hohenschwangau.de/'
    }

    r = requests.post('https://shop.ticket-center-hohenschwangau.de/Shop/PerformResUpdate2/de-DE/39901/', data=json.dumps(params), headers=headers)

    html = r.json()['szContent']
    soup = BeautifulSoup(html, 'html.parser')   

    if len(soup.select("h5")) > 0 or (len(soup.select('.InfoText')) > 0):
        # No free slots
        print("No free slots")
    else:
        print("found")
        l = ""
        for i in soup.select('.radioRowI .txt-sm'):
            print(i.text)
            l = l + i.text + '\n'

        push(castle['name'], l)    
        
    with open('test.html', 'w') as f:
        f.write(html)        


# %%
def push(title, msg):
    payload = {
        "token": config["PUSH_TOKEN"],
        "user": config["PUSH_USER"],
        "title": title,
        "message": msg
    }

    requests.post('https://api.pushover.net/1/messages.json', data=payload)


# %%
check_for_free_tickets("08.10.2021", CASTLES['Hohenschwangnau'])
check_for_free_tickets("09.08.2021", CASTLES['Hohenschwangnau'])
check_for_free_tickets("08.08.2021", CASTLES['Neuschwanstein'])
check_for_free_tickets("09.08.2021", CASTLES['Neuschwanstein'])


# %%



# %%



