import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets_new = tweets[tweets['content'].str.len() > 15][['tweet_id']]
    return tweets_new
    