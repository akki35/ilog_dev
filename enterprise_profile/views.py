from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from enterprise_profile.forms import EnterpriseProfileForm
from enterprise_profile.models import EnterpriseProfile
from enterprise.models import Enterprise
from accounts.models import MyUser
from nodes.models import Node
from django.core.urlresolvers import reverse


@login_required
def enterprise_profile_edit(request, slug):
    enterprise = request.user.enterprise
    page_enterprise = get_object_or_404(Enterprise, slug=slug)    
    if request.method == 'POST':
        
        form = EnterpriseProfileForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            about = form.cleaned_data.get('about')
            contact = form.cleaned_data.get('contact')
            website = form.cleaned_data.get('website')
            address = form.cleaned_data.get('address')
            capabilities = form.cleaned_data.get('capabilities')
            people_detail = form.cleaned_data.get('people_detail')
            product_intro = form.cleaned_data.get('product_intro')

            ep = EnterpriseProfile.objects.get(enterprise=enterprise)

            ep.image = image
            ep.image_thumbnail = image
            ep.address = address
            ep.contact = contact
            ep.about = about
            ep.website = website
            ep.capabilities = capabilities
            ep.people_detail = people_detail
            ep.product_intro = product_intro
            ep.save()

            myuser = request.user
            edit_post = u'{0} from {1} has edited the enterprise profile.'.format(myuser.first_name, myuser.enterprise)
            node = Node(myuser=myuser, post=edit_post)
            node.save()

            myuser.myuserprofile.notify_edited(enterprise=enterprise, node=node)

            return redirect('/enterprise/'+ slug)
        else:
            print('wtf')

    else:
        form = EnterpriseProfileForm(instance=enterprise, initial={
            'about': enterprise.enterpriseprofile.about,
            'address': enterprise.enterpriseprofile.address,
            'contact': enterprise.enterpriseprofile.contact,
            'website': enterprise.enterpriseprofile.website,
            'image': enterprise.enterpriseprofile.get_image,
            'capabilities': enterprise.enterpriseprofile.capabilities,
            'people_detail': enterprise.enterpriseprofile.people_detail,
            'product_intro': enterprise.enterpriseprofile.product_intro,
            })
    return render(request, 'enterprise_profile/enterprise_profile_edit.html', {'form':form,'page_enterprise':page_enterprise})


def enterprise_profile(request, slug):
    # slug = request.user.slug
    myuser = request.user
    page_enterprise = get_object_or_404(Enterprise, slug=slug)
    members = MyUser.objects.filter(enterprise=page_enterprise)

    return render(request, 'enterprise_profile/enterprise_profile.html', {
        'page_enterprise': page_enterprise,
        'profile':EnterpriseProfile.objects.get(enterprise=page_enterprise),
        'members': members,
        'slug': slug,
        'myuser': myuser
        })
    # return HttpResponseRedirect(reverse('enterprise:enterprise_profile'),  {
    #     'page_enterprise': page_enterprise,
    #     'members': members,
    #
    #     'args': slug,
    #     }, args=(slug,))

def enterprise_profile_aj(request, slug):
    # slug = request.user.slug
    myuser = request.user
    page_enterprise = get_object_or_404(Enterprise, slug=slug)
    members = MyUser.objects.filter(enterprise=page_enterprise)

    return render(request, 'enterprise_profile/enterprise_profile_aj.html', {
        'page_enterprise': page_enterprise,
        'profile':EnterpriseProfile.objects.get(enterprise=page_enterprise),
        'members': members,
        'slug': slug,
        'myuser': myuser
        })

# Create your views here.