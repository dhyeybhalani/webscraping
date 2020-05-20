import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/")
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')
mega_link = links + links2
mega_subtext = subtext + subtext2
def sorted_votes(hn):
    return sorted( hn , key = lambda k:k['votes'],reverse=True)


def get_info(links,subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href' , None)
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points',' '))
            if points > 99:
                hn.append({'title':title,'links':href,'votes':points})
    return sorted_votes(hn)

pprint.pprint(get_info(mega_link,mega_subtext))
