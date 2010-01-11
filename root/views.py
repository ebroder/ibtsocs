from django.shortcuts import get_object_or_404, redirect, render_to_response

from ibtsocs.root.models import Post, Vote

def index(request):
    posts = Post.objects.order_by('-created')[:10]
    return render_to_response('root/index.html',
                              {'posts': posts,
                               'visitor': request.session.session_key})

def display(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render_to_response('root/display.html',
                              {'post': post,
                               'visitor': request.session.session_key})

def vote(request, post_id, direction):
    post = get_object_or_404(Post, pk=post_id)
    visitor_id = request.session.session_key
    if not post.voted(visitor_id):
        v = Vote(post_id=post.id,
                 visitor_id=visitor_id,
                 vote_up=(direction == 'up'))
        v.save()
    return redirect(request.META.get('HTTP_REFERER', post))
