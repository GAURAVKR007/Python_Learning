import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')
age = soup.select('.age')
age2 = soup2.select('.age')

mega_links = links + links2
mega_subtext = subtext + subtext2
mega_age = age + age2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['Votes'],reverse=True)

def create_custom_hackernews(links,votes,age):
    hn = []
    for idx,item in enumerate(links):
        title = item.getText()
        href = item.a['href']
        vote = votes[idx].select('.score')
        time = age[idx].getText()
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 75:
                hn.append({'title': title,'Link' : href, 'Votes' : points, 'Time' : time})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hackernews(mega_links,mega_subtext,mega_age))
# create_custom_hackernews(links,subtext)
