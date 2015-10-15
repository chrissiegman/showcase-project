from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=10000)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=100)