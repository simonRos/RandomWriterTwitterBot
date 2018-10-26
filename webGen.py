#!/usr/bin/python3

from WordWeb import *
from conn import *
import tweepy

api = connect()

target_user = 'USATODAY'

coupled_chars = { '(' : ')',
                  '<' : '>',
                  '“' : '”',
                  '"' : '"',
                  "'" : "'" }

ww = WordWeb()
for status in tweepy.Cursor(api.user_timeline,
                                  screen_name = target_user,
                                  include_rts = False,
                                  tweet_mode = 'extended').items():
    tweet = status._json
    last = None
    processed_tweet = tweet['full_text'].replace('\n',' ').split(' ')
    #replace problematic characters
    for t in processed_tweet:
        if len(t) > 0:
            if t[0] in coupled_chars:
                if t[:-1] != coupled_chars[t[0]] or len(t) >= 1:
                    for c in coupled_chars:
                        t = t.replace(c,'')
            if t.replace(' ','') != '':
                ww.add(last, t)
                last = t
