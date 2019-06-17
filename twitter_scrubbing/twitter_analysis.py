import csv
import tweepy
from textblob import TextBlob
import json
import pandas as pd
import re

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_KEY']
    access_secret = info['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# passing the auth to tweepy API which provide gateway to tweets
api = tweepy.API(auth)


def remove_url(txt):
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with urls removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())


# opening a csv file
csvFile = open('results.csv', 'a')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['created_at', 'tweet', 'sentiment'])
search_term = "#AAPL -filter:retweets"

# receiving keyword you want to search for
public_tweets = tweepy.Cursor(api.search,
                              q=search_term,
                              lang="en",
                              since='2019-05-01').items(1000)
print(public_tweets)
# running a for loop to iterate over tweets and printing one row at a time

for tweet in public_tweets:
    print(tweet)
    # write in a csv file
    tweet_text = remove_url(tweet.text)
    analysis = TextBlob(tweet_text)
    csvWriter.writerow(
        [tweet.created_at, tweet_text, analysis.sentiment.polarity])
