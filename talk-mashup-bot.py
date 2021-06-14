#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 3
# ALA Talk generator

# This bot mashes up ALA talk titles to make new ones.
# First, it takes a list of talks from ALA Annual Meetings 2016-2021,
# and splits those titles into potential beginnings and endings.
# Then, it chooses a random beginning and a random ending, smushes 
# them together into a new talk title, and tweets it.

#Housekeeping
import random, string
import tweepy
from credentials import *
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def splitTitles(filename):
    """
    This function takes text file and splits each line in half.
    It returns two lists, first halves and second halves.
    """

    #open a text file
    talk_title_file = open(filename,'r',encoding='UTF-8')
    talk_titles = talk_title_file.readlines() #this creates a list: one line → one item
    talk_title_file.close()

    #create new blank lists
    beginners_list = []
    enders_list = []
    unsplit_titles = []

    #yet another list! this one is of the words we could split a title on
    split_at = ['at','of','for','on','and',':','!','?']

    #this next block of code is iterating over every talk title and splitting
    #them up where it can. it's slightly complex; don't feel like you have 
    #to be able to decipher it for now.
    for line in talk_titles:
        line = line.split() #turn title into a list of words
        i = -1
        for word in line:
            i += 1
            # if word[-1] == ':':
            #     beginners_list.append(line[0:i+1])
            #     enders_list.append(line[i+1:])
            # elif word[-1] == '?':
            #     beginners_list.append(line[0:i+1])
            #     enders_list.append(line[i+1:])
            # elif word[-1] == '!':
            #     beginners_list.append(line[0:i+1])
            #     enders_list.append(line[i+1:])
            if word.lower() in split_at:
                beginners_list.append(line[0:i+1])
                enders_list.append(line[i+1:])
            else:
                #unsplit_titles.append(line)
                if len(line) > 4: #titles of <5 words tend to be names, or might split uninterestingly
                    pass
                else:
                    mid = len(line) / 2 #find rough halfway point in line
                    mid = int(mid) #turn to integer
                    beginners_list.append(line[:mid])
                    enders_list.append(line[mid:])
                    #needsplitting.append(line)
    
    #oh look, even more lists!
    beginners_list_final = []
    enders_list_final = []
    for title in beginners_list:
        beginners_list_final.append(' '.join(title)) #stitch back into a phrase
    for title in enders_list:
        enders_list_final.append(' '.join(title)) #stitch back into a phrase

    return beginners_list_final, enders_list_final #this function spits out two lists



def main(): #this is a conventional Python thing. 
            #the main bit of the script is now in a function called main
    
    """
    This function randomly chooses a first half of a talk title and a second half
    of a talk title. Then it mashes them together and tweets it.
    """

    beginners = splitTitles('ala_all-talk-titles.txt')[0] 
    enders = splitTitles('ala_all-talk-titles.txt')[1]

    #find the length of the files (number of lines)
    beginners_length = len(beginners)
    enders_length = len(enders)

    #choose a random line by picking a number between 1 and the
    #number of lines in the files. (yes, it's a bit convoluted)
    title_first_part = beginners[random.randrange(1, beginners_length)]
    title_last_part = enders[random.randrange(1, enders_length)]

    #putting it all together: what's the new talk title?
    title = title_first_part + ' ' + title_last_part
    print(title)
    
    #tweet it
    api.update_status(title)
    print("Tweeted")


if __name__ == "__main__": 
	main() 
    #another conventional Python thing. don't worry, 
    # this bit makes no sense just looking at it

