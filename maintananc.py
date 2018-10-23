#!/usr/bin/python3

from conn import *
import tweepy

api = connect()

#follow back
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()


