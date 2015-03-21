from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from django.http import HttpResponse, HttpResponseBadRequest
from accounts.models import MyUser



@login_required
def inbox(request):
    conversations = Message.get_conversations(myuser=request.user)
    active_conversation = None
    messages = None
    if conversations:
        conversation = conversations[0]
        active_conversation = conversation['myuser'].slug
        messages = Message.objects.filter(myuser=request.user, conversation=conversation['myuser'])
        messages.update(is_read=True)
        for conversation in conversations:
            if conversation['myuser'].slug == active_conversation:
                conversation['unread'] = 0
    return render(request, 'messages/inbox.html', {
        'messages': messages,
        'conversations': conversations,
        'active': active_conversation
        })

@login_required
def messages(request, slug):
    conversations = Message.get_conversations(myuser=request.user)
    active_conversation = slug
    messages = Message.objects.filter(myuser=request.user, conversation__slug=slug)
    messages.update(is_read=True)
    for conversation in conversations:
        if conversation['myuser'].slug == slug:
            conversation['unread'] = 0
    return render(request, 'messages/inbox.html', {
        'messages': messages,
        'conversations': conversations,
        'active': active_conversation
        })

@login_required
def new(request):
    if request.method == 'POST':
        from_user = request.user
        to_user_username = request.POST.get('to')
        try:
            to_user = MyUser.objects.get(username=to_user_username)
        except:
            try:
                to_user_username = to_user_username[to_user_username.rfind('(')+1:len(to_user_username)-1]
                to_user = MyUser.objects.get(username=to_user_username)
            except:
                return redirect('/messages/new/')
        message = request.POST.get('message')
        if len(message.strip()) == 0:
            return redirect('/messages/new/')
        if from_user != to_user:
            Message.send_message(from_user, to_user, message)
        return redirect(u'/messages/{0}/'.format(to_user_username))
    else:
        conversations = Message.get_conversations(myuser=request.user)
        return render(request, 'messages/new.html', {'conversations': conversations})

@login_required
# @ajax_required
def delete(request):
    return HttpResponse()

@login_required
# @ajax_required
def send(request):
    if request.method == 'POST':
        from_user = request.user
        to = request.POST.get('to')

        to_user = MyUser.objects.get(slug=to)
        message = request.POST.get('message')
        if len(message.strip()) == 0:
            return HttpResponse()
        if from_user != to_user:
            msg = Message.send_message(from_user, to_user, message)
            return render(request, 'messages/inbox.html', {'message': msg})
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

@login_required
# @ajax_required
def users(request):
    myusers = MyUser.objects.filter(is_active=True)
    dump = []
    template = u'{0} ({1})'
    for myuser in myusers:
        if myuser.profile.get_screen_name() != myuser.username:
            dump.append(template.format(myuser.myuserprofile.get_screen_name(), myuser.username))
        else:
            dump.append(myuser.username)
    data =  dump                  #json.dumps(dump)
    return HttpResponse(data, content_type='application/json')

@login_required
# @ajax_required
def check(request):
    count = Message.objects.filter(myuser=request.user, is_read=False).count()
    return HttpResponse(count)


# Create your views here.
