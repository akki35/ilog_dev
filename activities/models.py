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
    # JOINED = 'J'
    ALSO_JOINED = 'K'
    EDITED = 'E'
    FOLLOWS = 'F'

    NOTIFICATION_TYPES = (
        (LIKED, 'Liked'),
        (COMMENTED, 'Commented'),
        (ALSO_COMMENTED, 'Also commented'),
        (ALSO_JOINED, 'Also joined'),
        (EDITED, 'Edited'),
        (FOLLOWS, 'Follows')
    )
    _LIKED_TEMPLATE = u'<a href="/user/{0}/">{1}</a> liked your post: <a href="/feeds/{2}/">{3}</a>'
    _COMMENTED_TEMPLATE = u'<a href="/user/{0}/">{1}</a> commented on your post: <a href="/feeds/{2}/">{3}</a>'
    _ALSO_COMMENTED_TEMPLATE = u'<a href="/user/{0}/">{1}</a> also commented on the post: <a href="/feeds/{2}/">{3}</a>'
    # _JOINED_TEMPLATE = u'<a href="/user/{0}/">{1}</a> has joined your enterprise'
    _ALSO_JOINED_TEMPLATE = u'<a href="/user/{0}/">{1}</a> also joined your enterprise'
    _EDITED_TEMPLATE = u'<a href="/user/{0}/">{1}</a> has made some edits to the enterprise profile'
    _FOLLOWS_TEMPLATE = u'<a href="/user/{0}/">{1}</a> from <a href="/enterprise/{2}/">{3}</a> is following you now'
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
                escape(self.from_user.slug),
                escape(self.from_user.get_full_name()),
                self.node.pk,
                escape(self.get_summary(self.node.post))
                )
        elif self.notification_type == self.COMMENTED:
            return self._COMMENTED_TEMPLATE.format(
                escape(self.from_user.slug),
                escape(self.from_user.get_full_name()),
                self.node.pk,
                escape(self.get_summary(self.node.post))
                )

        elif self.notification_type == 'S':
            return self._ALSO_COMMENTED_TEMPLATE.format(
                escape(self.from_user.slug),
                escape(self.from_user.get_full_name()),
                self.node.pk,
                escape(self.get_summary(self.node.post))
                )

        elif self.notification_type == 'F':
            return self._FOLLOWS_TEMPLATE.format(
                escape(self.from_user.slug),
                escape(self.from_user.get_full_name()),
                escape(self.from_user.enterprise.slug),
                escape(self.from_user.enterprise)
                )

        elif self.notification_type == 'K':
            return self._ALSO_JOINED_TEMPLATE.format(
                escape(self.from_user.slug),
                escape(self.from_user.get_full_name()),
                )

        elif self.notification_type == 'E':
            return self._EDITED_TEMPLATE.format(
                escape(self.from_user.slug),
                escape(self.from_user.get_full_name()),
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
