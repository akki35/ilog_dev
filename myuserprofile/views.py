from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, render_to_response
from enterprise.models import Enterprise, Operation
from accounts.models import MyUser
from django.contrib.auth.decorators import login_required
from nodes.views import nodes
from nodes.models import Node
from django.core.paginator import Paginator
from myuserprofile.forms import ProfileForm
from myuserprofile.models import MyUserProfile, Relationship
from django.core.urlresolvers import reverse
from django.template import RequestContext



def home(request):
    if request.user.is_authenticated():
        # nodes = Node.objects.all().order_by('-date')
        return nodes(request)
    else:
        return render(request, 'core/cover.html')

FEEDS_NUM_PAGES=8
@login_required
def network(request):
    myusers = MyUser.objects.all()
    enterprises = Enterprise.objects.all()
    return render(request, 'myuserprofile/network.html', {'myusers': myusers, 'enterprises':enterprises})

# @login_required
def profile(request, slug):
    context = RequestContext(request)
    data = {}
    page_user = get_object_or_404(MyUser, slug=slug)
    all_feeds = Node.get_feeds().filter(myuser=page_user)
    # paginator = Paginator(all_feeds, FEEDS_NUM_PAGES)
    # feeds = paginator.page(1)
    # from_feed = -1
    # if feeds:
    #     from_feed = feeds[0].id

    # skillset = MyUserProfile.skillset_set.filter(myuserprofile_id=page_user.myuserprofile.id)

    try:
        relationship_status = Relationship.objects.get(to_user_id=page_user.myuserprofile.id,
                                                       from_user_id=request.user.myuserprofile.id).status
    except:
        relationship_status = 'none'
    # relationship_status = Relationship.objects.get(to_user_id=page_user.myuserprofile.id,
    #                                                from_user_id=request.user.myuserprofile.id).status

    data['relationship_status'] = relationship_status
    data['feeds'] = all_feeds
    data['page_user'] = page_user
    # data['skillset'] = skillset
    return render_to_response('myuserprofile/profile.html', data, context_instance=context)

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
            'skillset': MyUserProfile.skillset.objects.filter(myuserprofile_id=mup.id)

            })
    return render(request, 'myuserprofile/profile_edit.html', {'form': form})

@login_required
def follow(request):
    myuser = request.user
    if request.method == 'POST':
        to_user = MyUser.objects.get(id=request.POST['to_user']).myuserprofile
        rel, created = Relationship.objects.get_or_create(
            from_user=myuser.myuserprofile,
            to_user=to_user,
            defaults={'status': 'F'}
        )

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
		# 	return HttpResponse(status=200)
		# else:
		# 	return HttpResponseRedirect(reverse('said_user:profile', kwargs={'username': to_user.username}))
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
		# 	return HttpResponse(status=200)
		# else:
		# 	return HttpResponseRedirect(reverse('said_user:profile', kwargs={'username': to_user.username}))
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
		# 	return HttpResponse(status=200)
		# else:
		# 	return HttpResponseRedirect(reverse('said_user:profile', kwargs={'username': to_user.username}))

    else:
        return HttpResponseRedirect(reverse('main:home'))

# Create your views here.
