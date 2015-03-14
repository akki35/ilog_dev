from django.shortcuts import render, redirect, get_object_or_404
from nodes.models import Node
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from ilog_dev.decorators import ajax_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.core.context_processors import csrf
from activities.models import Activity


NODES_NUM_PAGES = 10

@login_required
def nodes(request):
    all_nodes = Node.get_feeds()
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
# @ajax_required
def post(request):
    last_feed = request.POST.get('last_feed')
    myuser = request.user
    csrf_token = str(csrf(request)['csrf_token'])
    node = Node()
    node.myuser = myuser
    post = request.POST['post']
    post = post.strip()
    if len(post) > 0:
        node.post = post[:255]
        node.save()
    html = _html_feeds(last_feed, myuser, csrf_token)
    return HttpResponse(html)

@login_required
# @ajax_required
def comment(request):

    if request.method == 'POST':

        node_id = request.POST['node']
        node = Node.objects.get(pk=node_id)
        post = request.POST['post']
        post = post.strip()
        if len(post) > 0:
            post = post[:255]
            myuser = request.user
            node.comment(myuser=myuser, post=post)
            myuser.myuserprofile.notify_commented(node)
            myuser.myuserprofile.notify_also_commented(node)

        return HttpResponseRedirect('/nodes/')
    else:
        node_id = request.GET.get('node')
        node = Node.objects.get(pk=node_id)
        return render(request, 'feeds/partial_feed_comments.html', {'node': node})

@login_required
# @ajax_required
def like(request):
    node_id = request.POST['node']
    node = Node.objects.get(pk=node_id)
    myuser = request.user
    like = Activity.objects.filter(activity_type=Activity.LIKE, node=node_id, myuser=myuser)
    if like:
        myuser.profile.unotify_liked(node)
        like.delete()
    else:
        like = Activity(activity_type=Activity.LIKE, feed=node_id, myuser=myuser)
        like.save()
        myuser.profile.notify_liked(node)
    return HttpResponse(node.calculate_likes())
