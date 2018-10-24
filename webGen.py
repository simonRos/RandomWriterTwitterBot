#!/usr/bin/python3

from WordWeb import *
from conn import *
import tweepy

api = connect()

target_user = 'USATODAY'

ww = WordWeb()
for status in tweepy.Cursor(api.user_timeline,
                                  screen_name = target_user,
                                  include_rts = False,
                                  tweet_mode = 'extended').items():
    tweet = status._json
    last = None
    processed_tweet = tweet['full_text'].replace('\n',' ').split(' ')
    for p in processed_tweet:
        if p.replace(' ','') != '':
            ww.add(last, p)
            last = p

print(count)
