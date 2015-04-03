from django.shortcuts import render, redirect, render_to_response, RequestContext
from django.contrib.auth import authenticate, logout
from accounts.forms import *
from accounts.models import MyUser
from nodes.models import Node
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


def logup(request):
    if request.method == 'POST':
        form = LogupForm(request.POST)
        if not form.is_valid():
            # return "form invalid"
            render(request, 'accounts/logup.html', {'form': form})
        else:

            email = form.cleaned_data.get('email')
            enterprise = form.cleaned_data.get('enterprise')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password')
            MyUser.objects.create_myuser(email=email, enterprise=enterprise, first_name=first_name, last_name=last_name,
                                         password=password,)
            myuser = authenticate(email=email, password=password)
            # myuser.backend = 'django.contrib.auth.backends.ModelBackend'
            # authenticate(email=email, password=password)
            login(request, myuser)
            welcome_post = u'{0}from {1} has joined the network.'.format(myuser.first_name, myuser.enterprise)
            node = Node(myuser=myuser, post=welcome_post)
            node.save()
            return redirect('/')
    else:
        return render(request, 'accounts/logup.html', {'form': LogupForm()})


#
# def login(request):
#     """
#     Log in view
#     """
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = authenticate(email=request.POST['email'], password=request.POST['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('/')
#     else:
#         form = AuthenticationForm()
#     return render_to_response('accounts/login.html', {
#         'form': form,
#     }, context_instance=RequestContext(request))

def logout(request):
    logout(request)
    return redirect('/login')