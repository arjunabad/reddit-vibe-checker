#!/bin/python3


import praw
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# adding reddit user data
reddit = praw.Reddit(
    client_id="YOUR INPUT REQUIRED. CHECK README",
    client_secret="YOUR INPUT REQUIRED. CHECK README",
    user_agent="YOUR INPUT REQUIRED. CHECK README"
)

# subreddit and posts required
subreddit_name = "cats"
posts_required = 100



# subreddit name and posts to search
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.new(limit = posts_required)


analyzer = SentimentIntensityAnalyzer()



# visit each post and take compound score and title score
data = []
for i in posts:
    title = i.title or ""
    body = i.selftext or ""

    combined_text = title + " " + body
    combined_score = analyzer.polarity_scores(combined_text)
    title_score = analyzer.polarity_scores(title)

    data.append({
        "title": title,
        "body": body,
        "created_utc": pd.to_datetime(i.created_utc, unit = "s"),
        "title_sentiment": title_score["compound"],
        "combined_sentiment": combined_score["compound"]

    })

# conver dictionary into dataframe and sort based on date
df = pd.DataFrame(data)
df.sort_values("created_utc", inplace=True)

# print sub's average sentiment
average_sentiment = df["combined_sentiment"].mean()

if average_sentiment >= 0.05:
    sentiment_label = 'Positive'
elif average_sentiment <= -0.05:
    sentiment_label = 'Negative'
else:
    sentiment_label= 'Netural'

print(f"Average r/{subreddit_name} vibe is {sentiment_label} with a score of {average_sentiment:.2f}\n")


# print top 3 positive or negetive post titles
top_pos = df.nlargest(3, "combined_sentiment")
print("🟢 Top 3 Most Positive Posts:")

for idx, row in top_pos.iterrows():
    print(f"{idx} - {row['title']}\nScore: {row['combined_sentiment']:.2f}\n")

print("🔴 Top 3 Most Negetive Posts:")

top_neg = df.nsmallest(3, "combined_sentiment")
for idx, row in top_neg.iterrows():
    print(f"{idx} - {row['title']}\nScore: {row['combined_sentiment']:.2f}\n")



# Plot a time series graph
#plt.figure(figsize=(10,5))
#plt.plot(df["created_utc"], df["combined_sentiment"], marker="o")
#plt.title("Reddit posts sentiment over time - r/" + subreddit_name)
#plt.xlabel("Date")
#plt.ylabel("sentiment score")
#plt.grid(True)
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()
