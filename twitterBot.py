'''
@author Vivian Youkana
@file
A positive quote bot. Inspired by Sargis Yonan vitamin D bot.
'''

import tweepy 
import time
import random
import sys

#API and stuff 
consumer_key = 'nBm6nfhskUsbtBnG3gjK7iBuq'
consumer_secret = '3FQ9JWC6DSIGcfdSt7Y87NhVi1DZp3Vp8CBM9SCIxss9n17Kg6'
access_token = '1510734506013048834-CG8rlAHQlBXv9xVHm1eovNpuEjyj9e'
access_token_secret = 'PJOoC2jvvxZKOI8VnLVDC399y3ddEtjIaay2RHcU3I1a4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitter_API = tweepy.API(auth)

#Open txt file with quotes
argfile = str(sys.argv[1])
filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

salutations = ["Hi ", "Hello ", "Hey ", "Howdy "]

fwers = tweepy.Cursor(twitter_API.followers).items()

def tweet_quote():
    fwers = tweepy.Cursor(twitter_API.followers).items()
    for follower in fwers:
       greet = random.choice(salutations)
       twitter_API.update_status(greet + "@" + follower.screen_name + "! " + random.choice(f))
       time.sleep(0.5)
       
tweet_quote()