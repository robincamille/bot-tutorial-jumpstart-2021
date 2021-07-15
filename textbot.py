#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 2
# Lines of text

# This bot tweets a text file line by line, waiting a
# given period of time between tweets.

# Try this with another .txt file of your choosing!


# Housekeeping: do not edit
import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# What the bot will tweet
filename = open('phrases_coined_by_shakespeare.txt','r') 
tweet_text = filename.readlines() #this creates a list: one line → one item
filename.close()

# loop through the tweet_list
for line in tweet_text[0:5]: # Will only write first 5 lines
    api.update_status(status=line)
    print(line)
    time.sleep(5) # Pause for 5 seconds

print("All done!")

# To quit early: CTRL+C and wait a few seconds
