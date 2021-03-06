from django.db import models
from django.db.models import Count

from django.contrib.auth.models import User


class LinkVoteCountManager(models.Manager):
    def get_queryset(self):
        return super(LinkVoteCountManager, self).get_queryset().annotate(votes=Count('vote')).order_by('-votes')


class Link(models.Model):
    title = models.CharField("Title", max_length=100)
    submitter = models.ForeignKey(User)
    submit_date = models.DateTimeField(auto_now_add=True)
    rank_score = models.FloatField(default=0.0)
    url = models.URLField("URL", max_length=250, blank=True)
    description = models.TextField(blank=True)
    with_votes = LinkVoteCountManager()
    objects = models.Manager()

    def __str__(self):
        return self.title

class Vote(models.Model):
    voter = models.ForeignKey(User)
    link = models.ForeignKey(Link)

    def __str__(self):
        return "%s upvoted %s" % (self.voter.username, self.link.title)
