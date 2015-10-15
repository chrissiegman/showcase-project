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

    key_list = []
    for i in range(0, 5):
        key_list.append("tweet_" + str(i))

    text_list = []
    for i in range(0, 5):
        text_list.append(tweets[i].text)

    print(type(key_list))
    print(key_list)

    print(type(text_list))
    print(text_list)

    text_dict = dict(zip(key_list, text_list))
    print(type(text_dict))
    print(text_dict)

    return(text_dict)