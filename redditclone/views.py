from django.shortcuts import render
from django.views.generic import ListView

from redditclone.models import Link

# Create your views here.
class LinkListView(ListView):
    model = Link
