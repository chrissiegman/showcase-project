from django.shortcuts import render, HttpResponse
from biebfeed import twitterbot
from biebfeed.models import TwitterTarget


def index(request):
    current_user = request.user
    twitter_targets = TwitterTarget.objects.filter(user__username__contains=current_user)

    master_tweet_dict = {}
    for target in twitter_targets:
        master_tweet_dict[target.target_username] = twitterbot.get_user_tweets(target.target_username)

    context_dict = {}
    context_dict['twitter_targets'] = twitter_targets
    context_dict['master_tweet_dict'] = master_tweet_dict

    print(master_tweet_dict)
    return render(request, 'biebfeed/index.html', context_dict)