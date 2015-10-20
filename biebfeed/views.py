from django.shortcuts import render, HttpResponse

from biebfeed import twitterbot

def index(request):
    context_dict = {}
    context_dict['biebtweets'] = twitterbot.get_user_tweets('justinbieber')
    context_dict['swifttweets'] = twitterbot.get_user_tweets('taylorswift13')

    return render(request, 'biebfeed/index.html', context_dict)

def testing(request):
    context_dict = {}
    context_dict['biebtweets'] = twitterbot.get_user_tweets('justinbieber')
    context_dict['swifttweets'] = twitterbot.get_user_tweets('taylorswift13')

    return render(request, 'biebfeed/testing.html', context_dict)
