from twitter_data_retriever import TwitterScrapping
from twitter_sentiment_analyser import TwitterAnalyser
import matplotlib.pyplot as plt
import pandas as pd

retriever = TwitterScrapping("AAPL", '2019-05-01')
data = retriever.get_stock_tweets()

twitter_analyser = TwitterAnalyser()
twitter_analyser.get_sentiment()

sentiment_df = pd.read_csv('twitter_sentiments.csv')
print(sentiment_df.head(5))
fig, ax = plt.subplots(figsize=(8, 6))

# Plot histogram of the polarity values
sentiment_df['polarity'].hist(bins=[-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1],
                              ax=ax,
                              color="green")

plt.title("Sentiments from Tweets on AAPL stock")
plt.show()
