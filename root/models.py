# -*- coding: utf-8 -*-

from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

import tagging

class Post(models.Model):
    message = models.CharField(
        max_length=255,
        verbose_name="Why are you bemoaning computer science today?"
        )
    nick = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name='Nickname'
        )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    submitted_from = models.IPAddressField()

    def short_message(self):
        if len(self.message) < 20:
            return self.message
        else:
            return self.message[:20].rsplit(' ', 1)[0] + u'…'
    short_message.short_description = 'Message'

    def __unicode__(self):
        return self.short_message()

    @models.permalink
    def get_absolute_url(self):
        return ('ibtsocs.root.views.display', [str(self.id)])

    def upvotes(self):
        return self.votes.filter(vote_up=True).count()

    def downvotes(self):
        return self.votes.filter(vote_up=False).count()

    def voted(self, visitor_id):
        try:
            v = self.votes.get(visitor__pk=visitor_id)
            return 1 if v.vote_up else -1
        except ObjectDoesNotExist:
            return 0

class Vote(models.Model):
    visitor = models.ForeignKey(Session)
    post = models.ForeignKey(Post, related_name='votes')
    vote_up = models.BooleanField()

    class Meta:
        unique_together = (('visitor', 'post'),)

tagging.register(Post)
