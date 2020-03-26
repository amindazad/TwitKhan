"""Retrieve Tweets, emmbedings and persists in the database"""

import tweepy
import basilica
from decouple import config
from .models import DB, Tweet, User

TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_API_KEY'), config('TWITTER_API_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'), config('TWITTER_ACCESS_TOKEN_SECRET'))

TWITTER = tweepy.API(TWITTER_AUTH)

BASILICA = basilica.Connection(config('BASILICA_API_KEY'))

#TODO - WRITE FUNCTIONS 
