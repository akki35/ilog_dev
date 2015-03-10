from django.shortcuts import render, redirect, get_object_or_404
from enterprise.models import Enterprise
from accounts.models import MyUser
from django.contrib.auth.decorators import login_required
from nodes.views import nodes
from nodes.models import Node
from django.core.paginator import Paginator
from myuserprofile.forms import ProfileForm
from myuserprofile.models import MyUserProfile


def home(request):
    if request.user.is_authenticated():
        # nodes = Node.objects.all().order_by('-date')
        return nodes(request)
    else:
        return render(request, 'core/cover.html')

FEEDS_NUM_PAGES=10
@login_required
def network(request):
    myusers = MyUser.objects.all()
    enterprises = Enterprise.objects.all()
    return render(request, 'myuserprofile/network.html', {'myusers': myusers, 'enterprises':enterprises})

@login_required
def profile(request, username):
    page_user = get_object_or_404(MyUser, username=username)
    all_feeds = Node.get_feeds().filter(user=page_user)
    paginator = Paginator(all_feeds, FEEDS_NUM_PAGES)
    feeds = paginator.page(1)
    from_feed = -1
    if feeds:
        from_feed = feeds[0].id
    return render(request, 'core/profile.html', {
        'page_user': page_user,
        'feeds': feeds,
        'from_feed': from_feed,
        'page': 1
        })

@login_required
def profile_edit(request):
    myuser = request.user
    if request.method == 'POST':

        form = ProfileForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print('fucku')
            # myuserprofile = ProfileForm.save(commit=False)
            # # myuserprofile.myuser = myuser
            # myuserprofile.image = form.cleaned_data['image']
            # myuserprofile.job_position = form.cleaned_data.get('job_position')
            # myuserprofile.gender = form.cleaned_data.get('gender')
            # myuserprofile.experience = form.cleaned_data.get('experience')
            # myuserprofile.summary = form.cleaned_data.get('summary')
            # myuserprofile.save()

            image = form.cleaned_data['image']
            gender = form.cleaned_data.get('gender')
            experience = form.cleaned_data.get('experience')
            summary = form.cleaned_data.get('summary')
            job_position = form.cleaned_data.get('job_position')
            # location = form.cleaned_data.get('location')
            # mup = MyUserProfile.objects.create(myuser=myuser, image=image, gender=gender, experience=experience,
            #                                    summary=summary, job_position=job_position)
            mup = MyUserProfile.objects.get(myuser=myuser)
            mup.image = image
            mup.gender = gender
            mup.summary = summary
            mup.experience = experience
            mup.job_position = job_position
            mup.save()
            return redirect('/')

        else:
            print('wtf')

    else:
        form = ProfileForm(instance=myuser, initial={
            'job_position': myuser.myuserprofile.job_position,
            'summary': myuser.myuserprofile.summary,
            'gender': myuser.myuserprofile.gender,
            'experience': myuser.myuserprofile.experience,
            'image': myuser.myuserprofile.image,
            })
    return render(request, 'myuserprofile/profile_edit.html', {'form':form})



# Create your views here.
