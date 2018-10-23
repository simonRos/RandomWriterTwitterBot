#!/usr/bin/python3

from WordWeb import *
import creds
import tweepy

auth = tweepy.OAuthHandler(creds.consumer_key, creds.consumer_secret)
auth.set_access_token(creds.access_token, creds.access_token_secret)
api = tweepy.API(auth)

target_user = 'USATODAY'
debug = False

ww = WordWeb()
for tweet in tweepy.Cursor(api.user_timeline,id=target_user).items():
    last = None
    processed_tweet = tweet.text.replace('\n',' ').split(' ')
    for p in processed_tweet:
        if p.replace(' ','') != '':
            ww.add(last, p)
            last = p

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
