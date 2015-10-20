from django.shortcuts import render, HttpResponse

from biebfeed import twitterbot



def index(request):
    context_dict = {}
    user_list = ['justinbieber', 'taylorswift13']


    for user in user_list:
        context_dict[user] = twitterbot.get_user_tweets(user)

    context_dict['user_list'] = user_list

    return render(request, 'biebfeed/index.html', context_dict)