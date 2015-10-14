from django.shortcuts import render, HttpResponse

from biebfeed import twitterbot

def index(request):

    return HttpResponse(twitterbot.print_user_tweet('justinbieber'))
    #return render(request, 'biebfeed/index.html', {})
