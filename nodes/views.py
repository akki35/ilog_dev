from django.shortcuts import render, redirect, get_object_or_404, render_to_response,RequestContext
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
    # csrf_token = (csrf(request)['csrf_token'])
    if request.method == 'POST':

        post = request.POST['post']
        myuser = request.user
        feed = Node.objects.create(post=post, myuser=myuser)
        feed.save()

        return HttpResponseRedirect('/')
    else:
        # html = _html_feeds(last_feed, myuser, csrf_token)
        # return HttpResponse(html)
        return HttpResponseRedirect('/')

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
    if request.method == 'POST':

        node_id = request.POST['node']
        node = Node.objects.get(pk=node_id)
        myuser = request.user

        try:
            like = Activity.objects.get(activity='L', node=node_id, myuser=myuser)
            myuser.myuserprofile.unotify_liked(node)
            like.delete()
        except Exception:
            Activity.objects.create(activity='L', node=node_id, myuser=myuser)

            likes = myuser.myuserprofile.notify_liked(node)

        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
