import tweepy, time, sys
from biebfeed import authinfo

# uses tweepy, authinfo to handle twitter authorizations
auth = tweepy.OAuthHandler(authinfo.consumer_key, authinfo.consumer_secret)
auth.set_access_token(authinfo.access_key, authinfo.access_secret)
api = tweepy.API(auth)

def print_user_info(screen_name):
    user = api.get_user(screen_name)
    print("User's name: ", user.name)
    print("Screen name: ", user.screen_name)
    print("Number of followers: ", user.followers_count)

# will only work if tweet_number <= 20
def get_user_tweet(screen_name):
    tweet = api.user_timeline(screen_name)
    print(type(tweet))
    print(type(tweet[0].text))
    print(tweet[0].text)
    return(tweet[0].text)

def get_user_tweets(screen_name):
    tweets = api.user_timeline(screen_name)
    tweet_texts = {}

    tweet_texts['first_tweet'] = tweets[0].text
    tweet_texts['second_tweet'] = tweets[1].text
    tweet_texts['third_tweet'] = tweets[2].text
    tweet_texts['fourth_tweet'] = tweets[3].text
    tweet_texts['fifth_tweet'] = tweets[4].text

    print(type(tweet_texts))

    return(tweet_texts)
