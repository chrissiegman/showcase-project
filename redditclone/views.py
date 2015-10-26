from django.shortcuts import render
from django.views.generic import ListView

from redditclone.models import Link

class LinkListView(ListView):
    model = Link()
    queryset = Link.with_votes.all()
    paginate_by = 5
