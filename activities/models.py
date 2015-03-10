from django.db import models
from accounts.models import MyUser
# from enterprise.models import Enterprise
# from nodes.models import Node
from django.utils.html import escape


class Activity(models.Model):
    myuser = models.ForeignKey(MyUser)
    LIKE = 'L'
    ACTIVITY_TYPES = (
        (LIKE, 'Like'), )
    activity = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    node = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.activity


class Notification(models.Model):
    LIKED = 'L'
    COMMENTED = 'C'
    ALSO_COMMENTED = 'S'

    NOTIFICATION_TYPES = (
        (LIKED, 'Liked'),
        (COMMENTED, 'Commented'),
        (ALSO_COMMENTED, 'Also commented')
    )
    _LIKED_TEMPLATE = u'<a href="/{0}/">{1}</a> liked your post: <a href="/feeds/{2}/">{3}</a>'
    _COMMENTED_TEMPLATE = u'<a href="/{0}/">{1}</a> commented on your post: <a href="/feeds/{2}/">{3}</a>'
    _ALSO_COMMENTED_TEMPLATE = u'<a href="/{0}/">{1}</a> also commented on the post: <a href="/feeds/{2}/">{3}</a>'
    from_user = models.ForeignKey(MyUser, related_name='+')
    to_user = models.ForeignKey(MyUser, related_name='+')
    date = models.DateTimeField(auto_now_add=True)
    node = models.ForeignKey('nodes.Node')
    notification_type = models.CharField(max_length=1, choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ('-date',)

    def __str__(self):
        if self.notification_type == self.LIKED:
            return self._LIKED_TEMPLATE.format(
                escape(self.from_user.first_name),
                escape(self.from_user.get_full_name()),
                self.node.pk,
                escape(self.get_summary(self.node.post))
                )
        elif self.notification_type == self.COMMENTED:
            return self._COMMENTED_TEMPLATE.format(
                escape(self.from_user.first_name),
                escape(self.from_user.get_full_name()),
                self.node.pk,
                escape(self.get_summary(self.node.post))
                )

        elif self.notification_type == self.AlSO_COMMENTED:
            return self._ALSO_COMMENTED_TEMPLATE.format(
                escape(self.from_user.first_name),
                escape(self.from_user.get_full_name()),
                self.node.pk,
                escape(self.get_summary(self.node.post))
                )

        else:
            return "Oops! something went wrong."

    def get_summary(self, value):
        summary_size = 50
        if len(value) > summary_size:
            return u'{0}...'.format(value[:summary_size])
        else:
            return value

# Create your models here.
