import tweepy
import time
import csv
import sys


consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def get_user_ids():
    handles = []
    with open("list.csv", "rb") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            for elem in row:
                handles.extend(elem.strip().split(','))

        for handle in handles:
            try:
                u = api.get_user(handle[1:-1])
                time.sleep(6)
                print u._json['id']
                sys.stderr.write(str(u._json['id']) + "\n")
            except Exception, e:
                print e

if __name__ == '__main__':
    get_user_ids()
