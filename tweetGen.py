#!/usr/bin/python3
from WordWeb import *
import webGen
import random

ww = webGen.ww

def traverse(node,tweet):
    """
    Randomly traverse the WordWeb
    """
    if node.ender == True or len(node.followers) <= 0:
        tweet += node.word
        return tweet
    else:
        tweet += node.word
        traverse(random.choice(list(node.followers)),tweet)

tweet = ''
first = WordNode(None)
while first.starter == False:
    first = ww.nodes[random.choice(list(ww.nodes))]
print(traverse(first,tweet))
