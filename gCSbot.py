#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time
import sys

CONSUMER_KEY = '#####'
CONSUMER_SECRET = '#####'
ACCESS_KEY = '#####'
ACCESS_SECRET = '#####'

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
