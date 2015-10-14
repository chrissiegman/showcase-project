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
def print_user_tweet(screen_name):
    tweet = api.user_timeline(screen_name)
    print(tweet[0].text)
    return(tweet[0].text)
