#|--------------------------------------------------|
#| quick 10 minute app I made to help me locate job |
#| openings at companies I want to work for         |
#| specified by a list titled urls in jobber(urls)  |
#|--------------------------------------------------|
def jobber(urls):
    import requests
    from bs4 import BeautifulSoup as bs
    r = [requests.get(url) for url in urls]
    text = [url.text for url in r]
    jobs = [bs(url).get_text() for url in text]
    positions = [
    'Data Scientist',
    'Data Analyst',
    'Analyst',
    'Product Analyst',
    'Database Analyst'
    ]
    all_jobs = str() # where aggregated text from all provided urls will be housed
    for x in range (0,len(jobs)):
        all_jobs += jobs[x] # aggregating all webpage text
    for company in companies:
        for x in positions:    
            if x in all_jobs:
                print 'Possible',x,'opening at', company
                
jobber(urls) # where urls is a list of urls containing job openings
