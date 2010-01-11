from django.shortcuts import render_to_response, get_object_or_404

from ibtsocs.root.models import Post

def index(request):
    posts = Post.objects.order_by('-created')[:10]
    return render_to_response('root/index.html', {'posts': posts})

def display(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render_to_response('root/display.html', {'post': post})
