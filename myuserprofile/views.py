from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, render_to_response
from enterprise.models import Enterprise
from accounts.models import MyUser
from django.contrib.auth.decorators import login_required
# from nodes.views import nodes
from nodes.models import Node
from django.core.paginator import Paginator
from myuserprofile.forms import ProfileForm
from myuserprofile.models import MyUserProfile, Relationship
from django.core.urlresolvers import reverse
from PIL import Image
from django.template import RequestContext


def home(request):
    if request.user.is_authenticated():
        feed_nodes = Node.get_feeds()
        comment_nodes = Node.objects.filter(myuser=request.user, category='C')
        c = {'user': request.user,
             'profile': MyUserProfile.objects.get(myuser=request.user),
             'feed_nodes': feed_nodes}
        return render_to_response('user_home.html', c, context_instance=RequestContext(request))
# <<<<<<< HEAD
# =======
    else:
        return render(request, 'home.html')

def activity(request):
    if request.user.is_authenticated():
        feed_nodes = Node.get_feeds()
        comment_nodes = Node.objects.filter(myuser=request.user, category='C')
        c = {'user': request.user,
             'profile': MyUserProfile.objects.get(myuser=request.user),
             'feed_nodes': feed_nodes}
        return render_to_response('user_home.html', c)
# >>>>>>> origin/master
    else:
        return render(request, 'home.html')

FEEDS_NUM_PAGES=8
@login_required
def network(request):
    myusers = MyUser.objects.all()
    enterprises = Enterprise.objects.all()
    return render(request, 'myuserprofile/network.html', {'myusers': myusers, 'enterprises':enterprises})

# @login_required
def profile(request, slug):
    context = RequestContext(request)
    page_user = get_object_or_404(MyUser, slug=slug)
    user = request.user
    page_user_profile = page_user.myuserprofile
    all_feeds = Node.get_feeds().filter(myuser=page_user)
    # paginator = Paginator(all_feeds, FEEDS_NUM_PAGES)
    # feeds = paginator.page(1)
    # from_feed = -1
    # if feeds:
    #     from_feed = feeds[0].id
    feed_nodes = Node.objects.filter(myuser=request.user, category='F')
    skillset = page_user_profile.skillset.all()

    try:
        relationship_status = Relationship.objects.get(to_user_id=page_user.myuserprofile.id,
                                                       from_user_id=request.user.myuserprofile.id).status
    except:
        relationship_status = 'none'
    # relationship_status = Relationship.objects.get(to_user_id=page_user.myuserprofile.id,
    #                                                from_user_id=request.user.myuserprofile.id).status
    data={'skillset': skillset,
          'relationship_status': relationship_status,
          'feeds': all_feeds,
          'user': user,
          'page_user': page_user,
          'page_user_profile': page_user_profile,
          'nodes': feed_nodes
    }
    return render_to_response('myuserprofile/profile.html', data, context_instance=context)

def skillset(request, slug):
    context = RequestContext(request)
    page_user = get_object_or_404(MyUser, slug=slug)
    page_user_profile = page_user.myuserprofile
    skillset = page_user_profile.skillset.all()
    data={'skillset':skillset}
    return render_to_response('myuserprofile/skillset.html', data, context_instance=context)

@login_required
def profile_edit(request):
    myuser = request.user
    mup = MyUserProfile.objects.get(myuser=myuser)
    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)
        # print(form.errors)

        if form.is_valid():

            image = form.cleaned_data.get('image')
            gender = form.cleaned_data.get('gender')
            experience = form.cleaned_data.get('experience')
            summary = form.cleaned_data.get('summary')
            job_position = form.cleaned_data.get('job_position')
            skillset = form.cleaned_data.get('skillset')


            mup.image = image
            mup.image_thumbnail = image
            mup.gender = gender
            mup.summary = summary
            mup.experience = experience
            mup.job_position = job_position
            mup.skillset = skillset
            mup.save()
            return redirect('/')

    else:
        form = ProfileForm(instance=myuser, initial={
            'job_position': myuser.myuserprofile.job_position,
            'summary': myuser.myuserprofile.summary,
            'gender': myuser.myuserprofile.gender,
            'experience': myuser.myuserprofile.experience,
            'image': myuser.myuserprofile.image,
            'skillset': mup.skillset.all()

            })
    return render(request, 'myuserprofile/profile_edit.html', {'form': form})

@login_required
def follow(request):
    myuser = request.user
    if request.method == 'POST':
        to_use = MyUser.objects.get(id=request.POST['to_user'])
        to_user = MyUser.objects.get(id=request.POST['to_user']).myuserprofile
        rel, created = Relationship.objects.get_or_create(
            from_user=myuser.myuserprofile,
            to_user=to_user,
            defaults={'status': 'F'}
        )
        if created:
            follow_post = u'{0}from {1} is now following you.'.format(myuser.first_name, myuser.enterprise)

            node = Node(myuser=myuser, post=follow_post)
            node.save()

            myuser.myuserprofile.notify_followed(user=to_use, node=node)

        if not created:
            rel.status = 'F'
            rel.save()

        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect(reverse('/'))

@login_required()
def block(request):
    if request.method == 'POST':
        to_user = MyUser.objects.get(id=request.POST['to_user'])
        rel, created = Relationship.objects.get_or_create(
            from_user=request.user.id,
            to_user=to_user,
            defaults={'status': 'blocked'}
        )

        if not created:
            rel.status = 'blocked'
            rel.save()
        # if request.is_ajax():
        #   return HttpResponse(status=200)
        # else:
        #   return HttpResponseRedirect(reverse('said_user:profile', kwargs={'username': to_user.username}))
    else:
        return HttpResponseRedirect(reverse('main:home'))

@login_required()
def unfollow(request):
    if request.method == 'POST':
        to_user = MyUser.objects.get(id=request.POST['to_user']).myuserprofile

        Relationship.objects.filter(
            from_user=request.user.myuserprofile,
            to_user=to_user).update(status='N')

        # if request.is_ajax():
        #   return HttpResponse(status=200)
        # else:
        #   return HttpResponseRedirect(reverse('said_user:profile', kwargs={'username': to_user.username}))
        print('why')
        return HttpResponseRedirect('/')

    else:

        return HttpResponseRedirect('/')

@login_required()
def unblock(request):

    if request.method == 'POST':
        to_user = MyUser.objects.get(id=request.POST['to_user'])

        rel = Relationship.objects.filter(
            from_user=request.user,
            to_user=to_user).update(status='none')

        # if request.is_ajax():
        #   return HttpResponse(status=200)
        # else:
        #   return HttpResponseRedirect(reverse('said_user:profile', kwargs={'username': to_user.username}))

    else:
        return HttpResponseRedirect(reverse('main:home'))

# Create your views here.