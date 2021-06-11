
# -*- coding: utf-8 -*-
# ALA Talk generator

# This bot mashes up ALA talk titles to make new ones.
# It uses several data files of programs from ALA Annual Conference
# 2016-2021, which have been split into potential beginnings and endings.

import random, string
# import tweepy
#  from alacredentials import *
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# api = tweepy.API(auth)

def main():

    infile = open('talk-mashup-bot-files/ala_beginners.txt','r')
    beginners_data = infile.readlines()
    infile.close()

    infile = open('talk-mashup-bot-files/ala_enders.txt','r')
    enders_data = infile.readlines()
    infile.close()

    #make new blank lists
    beginners = []
    enders = []

    #populate lists from each text source
    for line in beginners_data:
        beginners.append(line[:-1]) #[:-1] excludes the invisible line break
    for line in enders_data:
        enders.append(line[:-1])


    #find the length of the files (number of lines)
    beginners_length = len(beginners)
    enders_length = len(enders)

    #choose a random line by picking a number between 1 and the
    #number of lines in the files
    title_first_part = beginners[random.randrange(1, beginners_length)]
    title_last_part = enders[random.randrange(1, enders_length)]

    #putting it all together, what's the new talk title?
    title = title_first_part + ' ' + title_last_part
    print(title)
        
    #api.update_status(title)

if __name__ == "__main__":
	main()
