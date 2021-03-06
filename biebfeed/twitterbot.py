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

def get_user_tweets(screen_name):
    tweets = api.user_timeline(screen_name)

    text_list = []
    for i in range(0, 5):
        text_list.append(tweets[i].text)

    return(text_list)

