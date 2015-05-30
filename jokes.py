'''
I got jokes.
'''

import random
import time
import datetime
import sys

def charlietango():
    def spam_binary():
        lower = int(10**34)
        upper = int(10**35)
        random_number = random.randint(lower, upper)
        return bin(random_number)[2:]
    try:
        while True:
            print spam_binary()
            time.sleep(0.05)
    except KeyboardInterrupt:
        print ''
        print 'Confirm authorization:'
        secondary_pw = raw_input('>>>')
        if secondary_pw == 'abort':
            print 'Aborting authentication protocol...'
            time.sleep(1)
            print 'Resetting cache...'
            time.sleep(1)
            print 'Disconnecting from secure network...'
            time.sleep(1)
            print 'Goodbye.'
            sys.exit()
        else:
            while True:
                print 'Authentication failed.'
                print 'Returning to network...'
                time.sleep(2.5)
                charlietango()

def invalid():
    week = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday',
    5:'Saturday', 6:'Sunday'}    
    the_time = datetime.datetime.now().time()
    today = datetime.date.today()
    the_day = week[today.weekday()]    
    print 'Invalid authorization request...'
    print 'Access denied.'    
    print 'Recorded: Entry access attempt at {0} on {1}, {2}.'.format(the_time, the_day, today)
                
def main():                
    print 'Compiling resources...'
    
    time.sleep(1.5)
    
    print 'Confirm authorization:'
    
    pw_entry = raw_input('>>>')
    
    if pw_entry == 'abort':
        print 'Goodbye.'
        sys.exit()
    
    elif pw_entry == 'charlietango':    
        print 'Welcome...'
        time.sleep(1)
        print 'Press CTRL+C to abort protocol at any time.'
        time.sleep(2)
        charlietango()
    
    elif pw_entry == 'echozulu':
        echozulu()            
    
    else:
        invalid()
                
main()
