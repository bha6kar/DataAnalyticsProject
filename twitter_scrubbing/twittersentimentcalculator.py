# %%
import numpy as np
import pandas as pd
from textblob import TextBlob

pd.options.mode.chained_assignment = None

df = pd.read_csv("twitter.csv")
# %%
df.iloc[1][3]
df
# %%

# %%
n = 0
sentiment = 0
df["New sentiment"]["a"] = pd.Series(
    np.random.randn(len(df["sentiment"])), index=df.index
)

# %%
dfObj = df.assign(
    Marks=pd.Series(np.random.randn(len(df["sentiment"])), index=df.index),
    Total=pd.Series(np.random.randn(len(df["sentiment"])), index=df.index),
)
# %%
df
for i in range(len(df)):
    text = TextBlob(df.iloc[i][3])
    newsentiment = text.sentiment.polarity
    sentiment += df.iloc[i][4]
    n += 1
    df["New sentiment"][i] = newsentiment
df.to_csv("twitter_sentiments.csv")
print(n)
print(sentiment)
print(sentiment / n)


# %%
