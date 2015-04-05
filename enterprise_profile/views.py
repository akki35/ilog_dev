from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from enterprise_profile.forms import EnterpriseProfileForm
from enterprise_profile.models import EnterpriseProfile
from enterprise.models import Enterprise
from accounts.models import MyUser
from nodes.models import Node
from django.core.urlresolvers import reverse


@login_required
def enterprise_profile_edit(request):
    enterprise = request.user.enterprise
    if request.method == 'POST':

        form = EnterpriseProfileForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            about = form.cleaned_data.get('about')
            contact = form.cleaned_data.get('contact')
            website = form.cleaned_data.get('website')
            address = form.cleaned_data.get('address')

            ep = EnterpriseProfile.objects.get(enterprise=enterprise)

            ep.image = image
            ep.image_thumbnail = image
            ep.address = address
            ep.contact = contact
            ep.about = about
            ep.website = website
            ep.save()

            myuser = request.user
            edit_post = u'{0} from {1} has edited the enterprise profile.'.format(myuser.first_name, myuser.enterprise)
            node = Node(myuser=myuser, post=edit_post)
            node.save()

            myuser.myuserprofile.notify_edited(enterprise=enterprise, node=node)

            return redirect('/')
        else:
            print('wtf')

    else:
        form = EnterpriseProfileForm(instance=enterprise, initial={
            'about': enterprise.enterpriseprofile.about,
            'address': enterprise.enterpriseprofile.address,
            'contact': enterprise.enterpriseprofile.contact,
            'website': enterprise.enterpriseprofile.website,
            'image': enterprise.enterpriseprofile.image,
            })
    return render(request, 'enterprise_profile/enterprise_profile_edit.html', {'form':form})


def enterprise_profile(request, slug):
    # slug = request.user.slug
    myuser = request.user
    page_enterprise = get_object_or_404(Enterprise, slug=slug)
    members = MyUser.objects.filter(enterprise=page_enterprise)

    return render(request, 'enterprise_profile/enterprise_profile.html', {
        'page_enterprise': page_enterprise,
        'profile':EnterpriseProfile.objects.get(enterprise=page_enterprise),
        'members': members,
        'slug': slug
        })
    # return HttpResponseRedirect(reverse('enterprise:enterprise_profile'),  {
    #     'page_enterprise': page_enterprise,
    #     'members': members,
    #
    #     'args': slug,
    #     }, args=(slug,))


# Create your views here.