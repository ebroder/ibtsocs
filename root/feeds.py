from django.contrib.syndicates.feeds import Feed
from ibtsocs.root.models import Post

class PostFeed(Feed):
    title = 'IBTSOCS: I Bemoan The State Of Computer Science'
    link = '/'

    def items(self):
        return Post.objects.order_by('-created')[:25]
