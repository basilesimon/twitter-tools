# Deleted tweets monitoring

This is a collection of tools to monitor deleted tweets.

## Dependencies and install
* `git clone` this repo
* `pip install tweepy`
* `pip install MySQL-python` (but you might need to  `apt-get install build-essential python-dev libmysqlclient-dev`. I read it's easy to install on Max OS, with Homebrew)
* `pip install needle`
* You will need a comma-separated list of user IDs (see below), or a list of keywords you want to track. See all the other options in [the Docs](https://dev.twitter.com/streaming/reference/post/statuses/filter).
* Obviously, you will also need your developer access keys and things. Pop them in the placeholders accordingly in each file.

### Comma-separated list of user IDs
I use the wonderful [t from sferik](https://github.com/sferik/t), a command line tool for twitter shenanigans.
Usually, I have an account following all the people I want to track - but it also works with lists.

* `$ t followings [account] > list.csv`
* `python get_user_ids.py > ids.csv`

## Run the program
Then to run it:
* Run `streaming.py`. Constantly. If it doesn't run, it doesn't save the tweets.
* Run `nosetests screenshot.py --with-save-baseline --nocapture` periodically to grab the screenshots.
