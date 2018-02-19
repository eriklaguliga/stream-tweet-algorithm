from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import csv
import json
import django
import nltk



ckey = "xxxx"
csecret = "xxxx"
atoken = "xxxx"
asecret = "xxxx"

#a=[]
handle = open("history.txt","w")
class listener(StreamListener):

    def on_data(self, data):
        #print(data)
        all =  json.loads(data)
        # print(all)
        tweet = all['text']
        toke = nltk.word_tokenize(tweet)
        print(toke)
        #a.append(toke)
        #print(a)
        #a.append(tweet)
        # print(a)
        #print(tweet)
        # print(data)
        return(True)

    def on_error(self, status):
        print (status)
# class listener(StreamListener):
#
#     def on_data(self, data):
#         # handle.write(data)
#         # print(data)
#         alldata = json.loads(data)
#         tweet = alldata["text"]
#         username = alldata["user"]["screen_name"]
#         print((username,tweet))
#         return(True)
#
#     def on_error(self, status):
#         print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
runtime = 10
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['indonesia'])
time.sleep(runtime)
twitterStream.disconnect()

