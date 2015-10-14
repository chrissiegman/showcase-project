from django.shortcuts import render, HttpResponse

from biebfeed import twitterbot

def index(request):
    context_dict = twitterbot.get_user_tweets('justinbieber')

    return render(request, 'biebfeed/index.html', context_dict)
