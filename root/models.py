from django.db import models

import tagging

class Post(models.Model):
    message = models.CharField(max_length=255)
    nick = models.CharField(max_length=128, null=True)

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

tagging.register(Post)
