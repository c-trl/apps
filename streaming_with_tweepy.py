from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import time
import urllib
from bs4 import BeautifulSoup as bs
import pandas as pd
import sched, time

ckey = 'ckey'
csecret = 'csecret'
atoken = 'atoken'
asecret = 'asecret'

class listener(StreamListener):

    def on_data(self, data):
        try:
            tweet = bs(data.split(',"text":"')[1].split('","source')[0]).get_text()
            print tweet
            return True
        except BaseException, e:
            print 'failed ondata,',str(e)
            
    def on_error(self, status):
        print status
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

s = sched.scheduler(time.time, time.sleep)
def print_time(): print "From print_time", time.time()

print time.time()
s.enter(5,1, print_time, ())
s.enter(10,1, print_time, ())
twitterStream.filter(track=['Pacquiao'])
tweet = bs(data.split(',"text":"')[1].split('","source')[0]).get_text()
s.run()
print tweet
print time.time()
