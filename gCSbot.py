#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time
import sys

CONSUMER_KEY = 'n1MTLlo7QO6wF4RxG5a7TJxuQ'
CONSUMER_SECRET = 'PEYBJagwoyWPa6IKnpUC2XGW8aowLS603Hkk7Q9fvp1gnpPGO6'
ACCESS_KEY = '3125708770-vmSH6fxI58hJQBhLLehFNGuc7ipg3BlIvyM9k0R'
ACCESS_SECRET = 'ixP2zAUFH7tAF9uiwrHqgGO9eWR0TQyhLlLLoUSr3o3DN'

argfile = str(sys.argv[1])

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(status=line)
    time.sleep(3000)
