from django import template
from django.core.urlresolvers import reverse
from django.utils.html import conditional_escape

register = template.Library()

@register.simple_tag
def link_if_not_voted(post, visitor, vote_dir, text):
    text = conditional_escape(text)
    try:
        if not post.voted(visitor):
            url = reverse('ibtsocs.root.views.vote', args=(post.id, vote_dir))
            return '<a href="%s">%s</a>' % (url, text)
    except:
        pass
    return text
