import requests
from bs4 import BeautifulSoup as bs
import nltk
import re
import pandas as pd

base_url = 'https://www.kaggle.com'
url = 'https://www.kaggle.com/jobs?page='
pages = range(28)

def read_html(url):
    r = requests.get(url)
    html = r.text
    soup = bs(html)
    return soup

job_top = 'a href="'
job_bot = '" title'
#tag.split(job_top)[1].split(job_bot)[0]    

by_top = 'profilelink" href="'
by_bot = '" title'
#tag.split(by_top)[1].split(by_bot)[0]

df = pd.DataFrame()
job = list()
by = list()

for page in pages:
    soup = read_html(url+str(page))
    for tag in soup.find_all('div', class_='topiclist-topic-name jobs-name-col'):
        job.append(base_url+str(tag.prettify().split(job_top)[1].split(job_bot)[0]))
        by.append(base_url+str(tag.prettify().split(by_top)[1].split(by_bot)[0]))

df['job'] = job
df['by'] = by

search_include = ['python', 'intern', 'new york']
search_exclude = ['masters', 'master\'s', 'ms', 'phd', 'senior']

read = int()
count = int()
found = list()

for url in df['job']:
    soup = read_html(url)
    text = soup.get_text().lower()
    tokens = nltk.word_tokenize(text)
    read += 1
    print read, 'Page(s) Processed'
    if 'python' in tokens and search_exclude not in tokens:
        with open('test.txt', 'r') as reader:
            if url not in reader.read():
                with open('kagglejobs.txt', 'a') as f:
                    f.write(url)
                    f.write('\n')
