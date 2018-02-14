from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import csv
import json


ckey = "xxxx"
csecret = "xxxx"
atoken = "xxxx"
asecret = "xxxx"


class listener(StreamListener):

    def on_data(self, data):
        # print(data)
        print(data)
        # all =  json.loads(data)
        # print(all)
        # tweet = all['text']
        # print(tweet)
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
twitterStream.sample()
time.sleep(runtime)
twitterStream.disconnect()
