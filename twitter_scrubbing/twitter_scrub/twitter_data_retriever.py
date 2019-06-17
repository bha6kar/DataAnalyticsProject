import csv
import tweepy
from textblob import TextBlob
import json
import pandas as pd
import re


class TwitterScrapping:
    def __init__(self, tinker, start):
        self.tinker = tinker
        self.start = start

    def remove_url(self, txt):
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

    def get_stock_tweets(self):
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

        # opening a csv file
        csvFile = open('twitter_scrapping.csv', 'a')
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['created_at', 'tweet'])
        search_term = '#' + self.tinker + ' -filter:retweets'

        # receiving keyword you want to search for
        public_tweets = tweepy.Cursor(api.search,
                                      q=search_term,
                                      lang="en",
                                      since=self.start).items(1000)

        for tweet in public_tweets:
            # write in a csv file
            tweet_text = self.remove_url(tweet.text)
            csvWriter.writerow(
                [tweet.created_at, tweet_text])

        tweets = pd.read_csv('twitter_scrapping.csv')
        return tweets


if __name__ == "__main__":
    retriever = TwitterScrapping("AAPL", '2019-05-01')
    retriever.get_stock_tweets()
