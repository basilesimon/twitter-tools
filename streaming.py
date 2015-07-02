from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from save_to_db import save_to_db

# Authentication details.
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


# This is the listener, resposible for receiving data
class StdOutListener(StreamListener):

    def on_status(self, status):
        tweet_url = "http://twitter.com/" + status.user.screen_name + "/status/" + status.id_str
        print "TWEET", status.text
        print "URL", tweet_url
        save_to_db(status.user.screen_name, status.text, tweet_url, status.id_str)

    def on_error(self, status):
        print status

if __name__ == "__main__":
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    ids = []
    with open("ids.csv") as f:
        for row in f:
            ids.append(row)

    stream = Stream(auth, l)
    stream.filter(ids)
