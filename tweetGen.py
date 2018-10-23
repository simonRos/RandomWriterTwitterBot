#!/usr/bin/python3
from WordWeb import *
import webGen
import random

ww = webGen.ww

def traverse(node,raw_tweet):
    """
    Randomly traverse the WordWeb
    """
    if node.ender == True or len(node.followers) <= 0:
        raw_tweet.append(node.word)
        refined_tweet = ' '.join(raw_tweet)
        return (refined_tweet)
    else:
        raw_tweet.append(node.word)
        return traverse(random.choice(list(node.followers)),raw_tweet)

raw_tweet = []
first = WordNode(None)
while first.starter == False:
    first = ww.nodes[random.choice(list(ww.nodes))]

outTweet = traverse(first,raw_tweet)
print(outTweet)
