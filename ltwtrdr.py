import requests
from bs4 import BeautifulSoup as bs

print "Please enter the URL of the webpage you would like to read"
url = raw_input()

r = requests.get(url)
text = r.text

soup = bs(text)

print soup.get_text()
