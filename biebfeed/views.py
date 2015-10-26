from django.shortcuts import render, HttpResponse
from biebfeed import twitterbot
from biebfeed.models import TwitterTarget


def index(request):
    current_user = request.user
    context_dict = {}
    master_tweet_dict = {}

    if str(current_user) != 'AnonymousUser':

        print("current user is:" + str(current_user))

        twitter_targets = TwitterTarget.objects.filter(user__username__contains=current_user)

        for target in twitter_targets:
            master_tweet_dict[target.target_username] = twitterbot.get_user_tweets(target.target_username)

        context_dict['master_tweet_dict'] = master_tweet_dict

    else:
        master_tweet_dict['justinbieber'] = twitterbot.get_user_tweets('justinbieber')
        context_dict['master_tweet_dict'] = master_tweet_dict

    return render(request, 'biebfeed/index.html', context_dict)

def friends(request):
    current_user = request.user
    context_dict = {}

    friends = TwitterTarget.objects.filter(user__username__contains=current_user)
    friend_list = []

    for friend in friends:
        friend_list.append(friend.target_username)


    context_dict['friend_list'] = friend_list

    return render(request, 'biebfeed/friends.html', context_dict)

def delete_friend(request):
    return HttpResponse('friend removed')

def add_friend(request):
    return HttpResponse('friend added')
