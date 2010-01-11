# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.sessions.models import Session

import tagging

class Post(models.Model):
    message = models.CharField(max_length=255)
    nick = models.CharField(max_length=128, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    submitted_from = models.IPAddressField()

    def __unicode__(self):
        if len(self.message) < 20:
            return self.message
        else:
            return self.message[:20].rsplit(' ', 1)[0] + u'…'

class Vote(models.Model):
    visitor = models.ForeignKey(Session)
    post = models.ForeignKey(Post, related_name='votes')
    vote_up = models.BooleanField()

    class Meta:
        unique_together = (('visitor', 'post'),)

tagging.register(Post)
