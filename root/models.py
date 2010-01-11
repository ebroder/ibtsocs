# -*- coding: utf-8 -*-

from django.db import models

import tagging

class Post(models.Model):
    message = models.CharField(max_length=255)
    nick = models.CharField(max_length=128, null=True)

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        if len(self.message) < 20:
            return self.message
        else:
            return self.message[:20].rsplit(' ', 1)[0] + u'…'

tagging.register(Post)
