import csv
import json

import tweepy
from textblob import TextBlob

with open("twitter_credentials.json") as cred_data:
    info = json.load(cred_data)
    consumer_key = info["CONSUMER_KEY"]
    consumer_secret = info["CONSUMER_SECRET"]
    access_key = info["ACCESS_KEY"]
    access_secret = info["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# passing the auth to tweepy API which provide gateway to tweets
api = tweepy.API(auth)

# opening a csv file
csvFile = open("result.csv", "a")
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["created_at", "tweet", "sentiment"])
search_term = "#AAPL -filter:retweets"

# receiving keyword you want to search for
public_tweets = tweepy.Cursor(
    api.search, q=search_term, lang="en", since="2019-05-01"
).items(1000)

# running a for loop to iterate over tweets and printing one row at a time
for tweet in public_tweets:
    # write in a csv file
    analysis = TextBlob(tweet.text)
    csvWriter.writerow(
        [tweet.created_at, tweet.text.encode("utf-8"), analysis.sentiment.polarity]
    )
    print(tweet.text)

    print(analysis.sentiment)
