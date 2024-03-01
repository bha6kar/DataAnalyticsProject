import collections
import itertools
import json
import re
import warnings

import matplotlib.pyplot as plt
import networkx
import nltk
import pandas as pd
import seaborn as sns
import tweepy as tw
from nltk.corpus import stopwords
from textblob import TextBlob

warnings.filterwarnings("ignore")

sns.set(font_scale=1.5)
sns.set_style("whitegrid")

with open("twitter_credentials.json") as cred_data:
    info = json.load(cred_data)
    consumer_key = info["CONSUMER_KEY"]
    consumer_secret = info["CONSUMER_SECRET"]
    access_token = info["ACCESS_KEY"]
    access_token_secret = info["ACCESS_SECRET"]

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


def remove_url(txt):
    """Replace URLs found in a text string with nothing
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())


# Create a custom search term and define the number of tweets
search_term = "#AAPL -filter:retweets"

tweets = tw.Cursor(api.search, q=search_term, lang="en", since="2019-05-01").items(1000)

# Remove URLs
tweets_no_urls = [remove_url(tweet.text) for tweet in tweets]
# Create textblob objects of the tweets
sentiment_objects = [TextBlob(tweet) for tweet in tweets_no_urls]

sentiment_objects[0].polarity, sentiment_objects[0]
sentiment_values = [
    [tweet.sentiment.polarity, str(tweet)] for tweet in sentiment_objects
]

sentiment_values[0]


# Create dataframe containing the polarity value and tweet text
sentiment_df = pd.DataFrame(sentiment_values, columns=["polarity", "tweet"])
sentiment_df.to_csv("twittergg.csv")
print(sentiment_df.head())
