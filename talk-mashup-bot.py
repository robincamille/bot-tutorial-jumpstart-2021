#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 3
# ALA Talk generator

# This bot mashes up ALA talk titles to make new ones.
# First, it takes a list of talks from ALA Annual Meetings 2016-2021,
# and splits those titles half: beginnings and endings.
# Then, it chooses a random beginning and a random ending, smushes 
# them together into a new talk title, and tweets it.

#Housekeeping
import random, tweepy
from credentials import *
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# we're now making up our own function, a reusable piece of code
def splitTitles(myfile):
    """
    This function takes text file and splits each line in half.
    It returns two lists, first halves and second halves.
    """

    #open a text file
    talk_title_file = open(myfile,'r',encoding='UTF-8')
    talk_titles = talk_title_file.readlines() 
    talk_title_file.close()

    #create empty lists
    beginners_list = []
    enders_list = []

    for line in talk_titles:
        line = line.split() #turn the string into a list of words ['like','this']
        middle = len(line) / 2 #find a rough halfway point in line
        middle = int(middle) #turn that point into an integer instead of a decimal

        #stitch together the split-up words, one for the first half and one for the second
        beginner = " ".join(line[:middle]) #the join syntax sucks, no one can ever remember it
        ender = " ".join(line[middle:])
        
        #add the talk halves to the two lists
        beginners_list.append(beginner) 
        enders_list.append(ender)

    return beginners_list, enders_list #return = what the function spits out to use

    #this is the end of the splitTitles() function


# run the splitTitles function and separate the beginning and ending halves
# into two new lists, beginners and enders
beginners_and_enders = splitTitles('ala_all-talk-titles.txt')
beginners = beginners_and_enders[0] 
enders = beginners_and_enders[1]

# find the length of the lists (number of items)
beginners_length = len(beginners)
enders_length = len(enders)

# choose a random line by picking a number between 1 and the
# number of lines in the lists. (yes, it's convoluted)
title_first_part = beginners[random.randrange(1, beginners_length)]
title_last_part = enders[random.randrange(1, enders_length)]

# putting it all together: what's the new talk title?
tweet_text = title_first_part + ' ' + title_last_part
print(tweet_text)

# tweet it
api.update_status(tweet_text)
print("...Tweeted!")
    