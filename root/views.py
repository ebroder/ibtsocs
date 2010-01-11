from django.shortcuts import render_to_response, get_object_or_404

from ibtsocs.root.models import Post

def index(request):
    posts = Post.objects.order_by('-created')[:10]
    return render_to_response('root/index.html', {'posts': posts})
