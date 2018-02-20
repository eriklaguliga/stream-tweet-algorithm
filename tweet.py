from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import csv
import json
import django
import nltk



ckey = "lh4BVF4dluBnviQ3uMKY7uu2O"
csecret = "FXZX1atG6rpuCHn4h0LyAtH9MwQIre1NsmYYEc1xAovSOKlWhZ"
atoken = "62031992-fHdAZwWIFXXPEZwgYOHk0hcJiXM7I8GhNWgYZbFLt"
asecret = "mjX3gFex3KxjJgCrvtsfB9xozhnU8tJ4qJswlN0v0VAwQ"

a=[]
handle = open("history.txt","w")
class listener(StreamListener):
    def __init__(self,waktu=10):
        self.waktumulai = time.time()
        self.waktuselesai = self.waktumulai + waktu


    def on_data(self, data):
        if time.time()>= self.waktuselesai:
        #print(data)
            all =  json.loads(data)
        # print(all)
            tweet = all['text']
            toke = nltk.word_tokenize(tweet)
            words = nltk.FreqDist(toke)
            print(words)
            print(toke)
        #a.append(toke)
        #print(a)
        #a.append(tweet)
        # print(a)
        #print(tweet)
        # print(data)
            return(True)
        else:
            return (False)

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

mulai = time.time()


# if mulai - time.time() <= 1:
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
runtime = 10
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['indonesia'])
time.sleep(runtime)
twitterStream.disconnect()
# else:

