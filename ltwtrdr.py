#Run this in Python to (try to) get a text-only version of a webpage.
#
#Currently needs some refining, only using this to pull text from my blog for reading and revising purposes.
#It gets the job done, albeit not filtering out some code including isogram, stylesheet sections
#Also still has unicode-related issues.

import requests
from bs4 import BeautifulSoup as bs

print "Please enter the URL of the webpage you would like to read"
url = raw_input()

r = requests.get(url)
text = r.text

soup = bs(text)

print soup.get_text()
