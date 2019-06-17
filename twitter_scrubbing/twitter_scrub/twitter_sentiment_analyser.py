import pandas as pd
import numpy as np
from textblob import TextBlob


class TwitterAnalyser:

    def get_sentiment(self):
        stock_tweets = pd.read_csv("twitter_scrapping.csv")

        stock_tweets = stock_tweets.assign(polarity=pd.Series(
            np.random.randn(len(stock_tweets['tweet'])), index=stock_tweets.index), sentiment=pd.Series(
            np.random.randn(len(stock_tweets['tweet'])), index=stock_tweets.index))

        for i in range(len(stock_tweets)):
            text = TextBlob(stock_tweets.iloc[i][1])
            newsentiment = text.sentiment.polarity
            stock_tweets['polarity'][i] = newsentiment
            if newsentiment > 0.0:
                stock_tweets['sentiment'][i] = 'Positive'
            elif newsentiment < 0.0:
                stock_tweets['sentiment'][i] = 'Negative'
            else:
                stock_tweets['sentiment'][i] = 'Neutral'

        stock_tweets.to_csv("twitter_sentiments.csv")
