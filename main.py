from asyncore import loop
from curses.ascii import isdigit
from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {
    'authority': 'www.gosugamers.net',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.8',
    'referer': 'https://www.gosugamers.net/counterstrike/rankings',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.gosugamers.net/counterstrike/rankings/list?maxResults=50&page=2', headers=headers)


def splitresult(string):
    lsplit = string.split(maxsplit=1)
    rsplit = lsplit[1].rsplit(maxsplit=1)
    return (lsplit[0], rsplit[0], rsplit[1])

blahblah = []

for i in range(40):
    params = (
        ('maxResults', '50'),
        ('page', i),
    )
    response = requests.get('https://www.gosugamers.net/counterstrike/rankings/list', headers=headers, params=params)
    epic = BeautifulSoup(response.text, "lxml")
    

    teams = epic.select("ul.ranking-list a")

    teamsen = [team.get_text(" ", strip=True) for team in teams]
    for team in teamsen:
        splits = splitresult(team)
        blahblah.append(splits)

 
my_df = pd.DataFrame(blahblah)
my_df.to_csv('test.csv', index=False, header=["Rank", "Team", "Elo"])