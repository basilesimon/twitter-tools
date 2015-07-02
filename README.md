# Deleted tweets monitoring

This is a collection of tools to monitor deleted tweets, automate screenshoting, and archiving.

* `streaming.py` and `save_to_db.py` work together to grab a real-time streamed timeline from Twitter and save all the results in a database.
* All the tweets in the database are then screenshot by `screenshot.py`
* Finally, the `monitoring.py` worker crawls through the database and checks if the tweets have been deleted.
* I included `get_user_ids.py`, as the Twitter API often requires the ID, and not the screen name (eg not "@basilesimon").

## Dependencies and install
* `git clone` this repo
* `pip install tweepy`
* `pip install MySQL-python` (but you might need to  `apt-get install build-essential python-dev libmysqlclient-dev`. I read it's easy to install on Max OS, with Homebrew)
* `pip install needle`
* You will need a comma-separated list of user IDs (see below), or a list of keywords you want to track. See all the other options in [the Docs](https://dev.twitter.com/streaming/reference/post/statuses/filter).
* Obviously, you will also need your developer access keys and things. Paste them in the placeholders accordingly in each file.

### Comma-separated list of user IDs
I use the wonderful [t from sferik](https://github.com/sferik/t), a command line tool for twitter shenanigans.
Usually, I have an account following all the people I want to track - but it also works with lists.

* `$ t followings [account] > list.csv`
* `python get_user_ids.py > ids.csv`

## Run the program
Then to run it:
* Run `streaming.py`. Constantly. If it doesn't run, you're not saving the tweets.
* Run `nosetests screenshot.py --with-save-baseline --nocapture` periodically to grab the screenshots.
* Run `monitoring.py` periodically to check for deleted tweets.

You might want to consider running all these with `cron` on a server. Just saying.

## License
[PDD/ Unlicense](http://choosealicense.com/licenses/unlicense/)
