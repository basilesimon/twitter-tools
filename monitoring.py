import MySQLdb
import requests


db = MySQLdb.connect(host="",
                     user="",
                     passwd="",
                     db="",
                     charset="utf8")
list_of_tweets = []


def query(url):
    r = requests.get(url)
    if r.status_code != 200:
        return True
    else:
        print "Tweet still exists"


def read_database(db):
    cur = db.cursor()
    cur.execute("""SELECT * \
                FROM Tweets \
                WHERE Deleted=0""")

    for tweet in cur:
        list_of_tweets.append(tweet)
	print tweet
    return list_of_tweets


def check_tweet():
    for tweet in read_database(db):
        if query(tweet[3]) is True:
            cur = db.cursor()
            cur.execute("""UPDATE Tweets \
                      SET Deleted=1 \
                      WHERE Tweet_Id=%s""", [tweet[4]])
            db.commit()
            print "tweet deleted, id is", tweet[4]
            print "url is", tweet[3]


if __name__ == "__main__":
    check_tweet()
