# Uses the twitter API to pull data on the most recent tweets that use the hashtag #Bitcoin
def get_bitcoin_tweets():
    import tweepy
    import json
    import os
    import pandas as pd

    # Twitter API credentials
    consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
    consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
    access_key = os.environ.get("TWITTER_ACCESS_KEY")
    access_secret = os.environ.get("TWITTER_ACCESS_SECRET")

    # Print the above 4 variables to make sure they are correct
    print(consumer_key)
    print(consumer_secret)
    print(access_key)
    print(access_secret)

    # Create an OAuthHandler object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Set the access token and secret
    auth.set_access_token(access_key, access_secret)
    # Create a Twitter API object
    api = tweepy.API(auth)

    print(auth, api)

    # Get the most recent tweets that contain the hashtag #Bitcoin
    bitcoin_tweets = api.search_tweets("bitcoin", count=100, result_type="recent")

    # Create a dataframe with the tweet information
    df = pd.DataFrame(data=[tweet.text for tweet in bitcoin_tweets], columns=["Tweets"])

    # save the dataframe to a csv file
    df.to_csv("bitcoin_tweets.csv")


# This function uses the twitter API to find the most recent tweet from the user "TheHeroShep" and returns the text of the tweet
def get_the_hero_shep_tweet():
    import tweepy
    import json
    import os
    import pandas as pd

    # Twitter API credentials
    consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
    consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
    access_key = os.environ.get("TWITTER_ACCESS_KEY")
    access_secret = os.environ.get("TWITTER_ACCESS_SECRET")

    # Print the above 4 variables to make sure they are correct
    print(consumer_key)
    print(consumer_secret)
    print(access_key)
    print(access_secret)

    # Create an OAuthHandler object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Set the access token and secret
    auth.set_access_token(access_key, access_secret)
    # Create a Twitter API object
    api = tweepy.API(auth)

    print(auth, api)

    # Get the most recent tweets from the user "TheHeroShep"
    the_hero_shep_tweet = api.user_timeline(id="TheHeroShep", count=1)
    print(the_hero_shep_tweet)


# create a main function that calls get_bitcoin_tweets()
if __name__ == "__main__":
    # get_bitcoin_tweets()
    get_the_hero_shep_tweet()
