from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import csv
import json


ckey = "lh4BVF4dluBnviQ3uMKY7uu2O"
csecret = "FXZX1atG6rpuCHn4h0LyAtH9MwQIre1NsmYYEc1xAovSOKlWhZ"
atoken = "62031992-fHdAZwWIFXXPEZwgYOHk0hcJiXM7I8GhNWgYZbFLt"
asecret = "mjX3gFex3KxjJgCrvtsfB9xozhnU8tJ4qJswlN0v0VAwQ"


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
