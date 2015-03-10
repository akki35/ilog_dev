from django.shortcuts import render, redirect, get_object_or_404
from nodes.models import Node
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from ilog_dev.decorators import ajax_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.context_processors import csrf

NODES_NUM_PAGES = 10

@login_required
def nodes(request):
    all_nodes = Node.get_nodes()
    paginator = Paginator(all_nodes, NODES_NUM_PAGES)
    nodes = paginator.page(1)
    from_node = -1
    if nodes:
        from_node = nodes[0].id
    return render(request, 'nodes/nodes.html', {
        'nodes': nodes,
        'from_node': from_node,
        'page': 1,
        })
    # return all_nodes

def _html_feeds(last_feed, user, csrf_token, feed_source='all'):
    feeds = Node.get_feeds_after(last_feed)
    if feed_source != 'all':
        feeds = feeds.filter(user__id=feed_source)
    html = u''
    for feed in feeds:
        html = u'{0}{1}'.format(html, render_to_string('feeds/partial_feed.html', {
            'feed': feed,
            'user': user,
            'csrf_token': csrf_token
            })
        )
    return html

@login_required
@ajax_required
def post(request):
    last_feed = request.POST.get('last_feed')
    user = request.user
    csrf_token = unicode(csrf(request)['csrf_token'])
    feed = Node()
    feed.user = user
    post = request.POST['post']
    post = post.strip()
    if len(post) > 0:
        feed.post = post[:255]
        feed.save()
    html = _html_feeds(last_feed, user, csrf_token)
    return HttpResponse(html)