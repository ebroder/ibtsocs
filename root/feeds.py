from django.contrib.syndication.feeds import Feed
from ibtsocs.root.models import Post

class PostFeed(Feed):
    title = 'IBTSOCS: I Bemoan The State Of Computer Science'
    link = '/'

    def items(self):
        return Post.objects.order_by('-created')[:25]

    def item_author_name(self, item):
        return item.nick

    def item_pubdate(self, item):
        return item.created
