from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from enterprise_profile.forms import EnterpriseProfileForm
from enterprise_profile.models import EnterpriseProfile
from enterprise.models import Enterprise
from accounts.models import MyUser
# from somewhere import handle_uploaded_file


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
            ep.address = address
            ep.contact = contact
            ep.about = about
            ep.website = website
            ep.save()

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
        'members': members

        })


# Create your views here.
