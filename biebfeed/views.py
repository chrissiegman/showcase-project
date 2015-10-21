from django.shortcuts import render, HttpResponse
from biebfeed import twitterbot
from biebfeed.models import twitter_target


def index(request):
    context_dict = {}
    twitter_targets = twitter_target.objects.all()
    context_dict['twitter_targets'] = twitter_targets
    print(twitter_targets)

    for target in twitter_targets:
        context_dict['target_tweet_list'] = twitterbot.get_user_tweets(target.target_username)

    print(context_dict)
    return render(request, 'biebfeed/index.html', context_dict)