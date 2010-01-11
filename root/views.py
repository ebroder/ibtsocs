from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404, redirect, render_to_response

from ibtsocs.root.models import Post, Vote

def index(request):
    post_list = Post.objects.order_by('-created')
    paginator = Paginator(post_list, 25)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

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
