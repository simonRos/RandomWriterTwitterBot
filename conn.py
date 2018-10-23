#!/usr/bin/python3

import creds
import tweepy

def connect():
    auth = tweepy.OAuthHandler(creds.consumer_key, creds.consumer_secret)
    auth.set_access_token(creds.access_token, creds.access_token_secret)
    api = tweepy.API(auth)
    return api
