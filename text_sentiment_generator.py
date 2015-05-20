import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import nltk
from nltk.corpus import stopwords

def get_website_text(url):    
    r = requests.get(url)
    html = r.text
    
    def trim_html(html):
        remove_head = '<body>'
        remove_footer = '</body>'
        try:
            return html.split(remove_head)[1].split(remove_footer)[0]
        except BaseException, e:
            print 'Notice: The provided URL does not contain appropriate HTML <body> tags'
            return html
        
    body = trim_html(html)        
    soup = bs(body).get_text()
    
    return soup
    
def get_pos_words(): 
    pos_words_url = 'https://raw.githubusercontent.com/c-trl/apps/master/positive_wordbank.txt'
    pos_wordbank = get_website_text(pos_words_url)
    pos_words = nltk.word_tokenize(pos_wordbank)
    return pos_words
    
def get_neg_words(): 
    neg_words_url = 'https://raw.githubusercontent.com/c-trl/apps/master/negative_wordbank.txt'    
    neg_wordbank = get_website_text(neg_words_url)
    neg_words = nltk.word_tokenize(neg_wordbank)
    return neg_words 
   
def tokenize_text(text):    
    tokens = nltk.word_tokenize(text)
    tokens = [token for token in tokens if token.isalpha() == True]
    return tokens

def get_sentiment(tokens): #tokens must be a list() object
    from nltk.corpus import stopwords
    
    pos_sentiment = float()
    neg_sentiment = float()
    neutral = float()
    stopwords = stopwords.words('english')
    total = float(len(tokens))
    
    for token in tokens:
        if token not in stopwords:
            if token in pos_words:
                pos_sentiment += 1
            elif token in neg_words:
                neg_sentiment += 1
            else:
                neutral += 1
        else:
            pass
    
    if pos_sentiment > neg_sentiment:
        sentiment = pos_sentiment / total
        print 'Text contains positive sentiment'
        print round(sentiment, 2)
        return sentiment
    elif pos_sentiment < neg_sentiment:
        sentiment = neg_sentiment / total
        print 'Text contains negative sentiment'
        print round(sentiment, 2)
        return sentiment
    else: #pos = neg
        print 'Text contains neutral sentiment'
        print 'Negative words:'
        for token in tokens:
            if token in neg_words:
                print token
        print 'Positive words:'
        for token in tokens:
            if token in pos_words:
                print token                

url = raw_input('Bonjour!  Por favor, enter the URL(s) of a website whose sentiment you want to analyze.  Separate multiple URLs with a \',\'.\n>')  

try:
    text = get_website_text(url)
    pos_words = get_pos_words()
    neg_words = get_neg_words()
    tokens = tokenize_text(text)
    get_sentiment(tokens)   
except BaseException, e:
    print 'Error:', str(e)
    print 'Please try another valid URL'
