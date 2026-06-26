# Twitter Sentiment Analysis

import os
import re
import nltk
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download required NLTK resources
nltk.download("vader_lexicon")
nltk.download("words")

# Load dataset
# Replace this path with your dataset location
df = pd.read_csv("data_science-tweet.csv", low_memory=False)

# Initialize VADER
sid = SentimentIntensityAnalyzer()

# English dictionary
words = set(nltk.corpus.words.words())


def cleaner(tweet):
    """
    Clean tweet by removing usernames, URLs, hashtags,
    and non-English words.
    """
    tweet = re.sub("@[A-Za-z0-9]+", "", tweet)
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet)
    tweet = " ".join(tweet.split())
    tweet = tweet.replace("#", "").replace("_", " ")

    tweet = " ".join(
        w for w in nltk.wordpunct_tokenize(tweet)
        if w.lower() in words or not w.isalpha()
    )

    return tweet


# Clean tweets
df["tweet_clean"] = df["tweet"].apply(cleaner)

# Custom sentiment dictionary
word_dict = {
    "manipulate": -1,
    "manipulative": -1,
    "jamescharlesiscancelled": -1,
    "jamescharlesisoverparty": -1,
    "pedophile": -1,
    "pedo": -1,
    "cancel": -1,
    "cancelled": -1,
    "cancel culture": 0.4,
    "teamtati": -1,
    "teamjames": 1,
    "teamjamescharles": 1,
    "liar": -1,
}

# Update VADER lexicon
sid.lexicon.update(word_dict)

# Calculate sentiment score
sentiment_scores = []

for tweet in df["tweet_clean"]:
    score = sid.polarity_scores(str(tweet))["compound"]
    sentiment_scores.append(score)

df["sentiment"] = sentiment_scores


def sentiment_category(score):
    """Convert compound score into sentiment label."""
    if score > 0:
        return "positive"
    elif score == 0:
        return "neutral"
    else:
        return "negative"


df["sentiment_category"] = df["sentiment"].apply(sentiment_category)

# Keep useful columns
df = df[["tweet", "date", "id", "sentiment", "sentiment_category"]]

# Count positive tweets
positive = (
    df[df["sentiment_category"] == "positive"]
    .groupby("date", as_index=False)
    .count()[["date", "id"]]
)

# Count negative tweets
negative = (
    df[df["sentiment_category"] == "negative"]
    .groupby("date", as_index=False)
    .count()[["date", "id"]]
)

# Plot results
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=positive["date"],
        y=positive["id"],
        mode="markers+lines",
        name="Positive Tweets",
        line_color="green",
    )
)

fig.add_trace(
    go.Scatter(
        x=negative["date"],
        y=negative["id"],
        mode="markers+lines",
        name="Negative Tweets",
        line_color="red",
    )
)

fig.update_layout(
    title="Twitter Sentiment Analysis",
    xaxis_title="Date",
    yaxis_title="Number of Tweets",
    template="plotly_white",
)

fig.show()
