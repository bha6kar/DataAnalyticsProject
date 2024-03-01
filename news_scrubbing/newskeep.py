from collections import deque

import apiprocessing
import numpy as np
import pandas as pd

datax = deque()
for story in apiprocessing.stories:
    x = list()
    x.append(story.title)
    x.append(story.source.name)
    x.append(story.published_at.date())
    x.append(story.sentiment.title.score)
    x.append(story.sentiment.body.score)
    x.append(" ".join(story.summary.sentences))
    print(story.summary.sentences)
    x.append(story.links.permalink)
    datax.append(x)

storage = np.array(datax)
datax = np.array(datax)

headers = ["Title", "Source", "Date", "Title Sentiment", "Body Sentiment", "Summary"]
df = pd.DataFrame(
    data=datax[0:, 0:],
    columns=[
        "Title",
        "Source",
        "Date",
        "Title Sentiment",
        "Body Sentiment",
        "Summary",
        "Link",
    ],
)
df.index += 1
df.to_csv("export.csv")

print("\n")
print("Collected Articles are written in export.csv")
