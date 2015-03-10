from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from enterprise_profile.forms import EnterpriseProfileForm
from enterprise_profile.models import EnterpriseProfile


@login_required
def enterprise_profile_edit(request):
    enterprise = request.user.enterprise
    if request.method == 'POST':

        form = EnterpriseProfileForm(request.POST)
        print(form.errors)
        if form.is_valid():
            image = form.cleaned_data['image']
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




# Create your views here.
