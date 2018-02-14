import tweepy
import time
from tweepy import Stream, StreamListener, OAuthHandler

ckey = "lh4BVF4dluBnviQ3uMKY7uu2O"
csecret = "FXZX1atG6rpuCHn4h0LyAtH9MwQIre1NsmYYEc1xAovSOKlWhZ"
auth = OAuthHandler(ckey,csecret)

runtime = 10

a = Stream(auth,StreamListener())
tweepy.
