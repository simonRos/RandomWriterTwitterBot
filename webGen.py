#!/usr/bin/python3

from WordWeb import *
from conn import *
import tweepy

api = connect()

target_user = 'USATODAY'
debug = False
debug_limit = 10
debug_count = 0

ww = WordWeb()
for tweet in tweepy.Cursor(api.user_timeline,id=target_user).items():
    if debug_count < debug_limit:
        last = None
        processed_tweet = tweet.text.replace('\n',' ').split(' ')
        for p in processed_tweet:
            if p.replace(' ','') != '':
                ww.add(last, p)
                last = p
    else:
        break;
    debug_count += 1

if debug == True:
    with open("web.txt", 'w') as debugFile:
        for k,v in ww.nodes.items():
            try:
                debugFile.write(str(k))
                debugFile.write('\t'+str(len(v.followers))+'\n')
                for f in v.followers:
                    debugFile.write('\t'+f.word)
                    debugFile.write('\n\t\t'+str(v.followers[f])+'\n')
            except:
                pass
