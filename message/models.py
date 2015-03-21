from django.db import models
from accounts.models import MyUser
from django.db.models import Max


class Message(models.Model):
    myuser = models.ForeignKey(MyUser, related_name='+')
    message = models.TextField(max_length=5000, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(MyUser, related_name='+')
    from_user = models.ForeignKey(MyUser, related_name='+')
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ('date',)

    def __str__(self):
        return self.message

    @staticmethod
    def send_message(from_user, to_user, message):
        message = message[:5000]
        current_user_message = Message(from_user=from_user,
                                       message=message,
                                       myuser=from_user,
                                       conversation=to_user,
                                       is_read=True)
        current_user_message.save()
        Message(from_user=from_user,
                conversation=from_user,
                message=message,
                myuser=to_user).save()
        return current_user_message

    @staticmethod
    def get_conversations(myuser):
        conversations = Message.objects.filter(myuser=myuser).values('conversation').annotate(last=Max('date'))\
            .order_by('-last')
        users = []
        for conversation in conversations:
            users.append({
                'myuser': MyUser.objects.get(pk=conversation['conversation']),
                'last': conversation['last'],
                'unread': Message.objects.filter(myuser=myuser, conversation__pk=conversation['conversation'],
                                                 is_read=False).count(),
                })
        return users


# Create your models here.
