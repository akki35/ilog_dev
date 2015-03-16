from django.db import models
from accounts.models import MyUser
from enterprise.models import Operation
from activities.models import Notification
# from nodes.models import Node
from django.db.models.signals import post_save


class MyUserProfile(models.Model):
    myuser = models.OneToOneField(MyUser)
    GenderChoices = (('M', 'Male'), ('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GenderChoices)
    skillset = models.ManyToManyField(Operation)
    job_position = models.CharField(max_length=255)
    experience = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    follows = models.ManyToManyField('self', through='Relationship', related_name='related_to', symmetrical=False)
    score = models.FloatField(default=0)
    image = models.ImageField(upload_to='user/main')
    # thumbnail = models.ImageField(upload_to='images/user/thumbnail')

    def __str__(self):
        return self.myuser.get_full_name()

    def get_screen_name(self):
        return self.myuser.get_full_name

    def get_image(self):
        default_image = 'user/main/user.jpg'
        if self.image:
            return self.image
        else:
            return default_image

    # def get_thumbnail(self):
    #     default = 'images/user/thumbnail/user.png'
    #     if self.thumbnail:
    #         return self.thumbnail
    #     else:
    #         return default

    def notify_liked(self, node):
        if self.myuser != node.myuser:
            Notification(notification_type=Notification.LIKED,
                         from_user=self.myuser,
                         to_user=node.myuser,
                         node=node).save()

    def unotify_liked(self, node):
        if self.myuser != node.myuser:
            Notification.objects.filter(notification_type=Notification.LIKED,
                                        from_user=self.myuser,
                                        to_user=node.myuser,
                                        node=node).delete()

    def notify_commented(self, node):
        if self.myuser != node.myuser:
            Notification(notification_type=Notification.COMMENTED,
                         from_user=self.myuser,
                         to_user=node.myuser,
                         node=node).save()

    def notify_also_commented(self, node):
        comments = node.get_comments()
        users = []
        for comment in comments:
            if comment.myuser != self.myuser and comment.myuser != node.myuser:
                users.append(comment.myuser.pk)
        users = list(set(users))
        for user in users:
            Notification(notification_type=Notification.ALSO_COMMENTED,
                         from_user=self.myuser,
                         to_user=MyUser(id=user),
                         node=node).save()

    # followers related things

    def add_relationship(self, person, status='F'):
        relationship, created = Relationship.active.get_or_create(
            from_person=self,
            to_person=person,
            status=status)
        return relationship

    def remove_relationship(self, person, status):
        Relationship.active.filter(
            from_person=self,
            to_person=person,
            status=status).delete()
        return

    def get_relationships(self, status):
        return self.relationships.filter(
            to_people__status=status,
            to_people__from_person=self)

    def get_related_to(self, status):
        return self.related_to.filter(
            from_people__status=status,
            from_people__to_person=self)

    def get_following(self):
        return self.get_relationships(RELATIONSHIP_FOLLOWING)

    def get_followers(self):
        return self.get_related_to(RELATIONSHIP_FOLLOWING)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyUserProfile.objects.create(myuser=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.myuserprofile.save()
    print("profile saved")

post_save.connect(create_user_profile, sender=MyUser)
post_save.connect(save_user_profile, sender=MyUser)


class ActiveRelationshipManager(models.Manager):
    def get_queryset(self):
        return super(ActiveRelationshipManager, self).get_queryset().filter(status='F')

RELATIONSHIP_FOLLOWING = 'F'
RELATIONSHIP_BLOCKED = 'B'


class Relationship(models.Model):

    RELATIONSHIP_STATUSES = ((RELATIONSHIP_FOLLOWING, 'Following'), (RELATIONSHIP_BLOCKED, 'Blocked'), )
    from_user = models.ForeignKey(MyUserProfile, related_name='from_person')
    to_user = models.ForeignKey(MyUserProfile, related_name='to_person')
    status = models.CharField(max_length=1, choices=RELATIONSHIP_STATUSES)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    active = ActiveRelationshipManager()

    class Meta:
        ordering = ('created',)
        verbose_name = ('relationship')
        verbose_name_plural = ('relationships')

    def __str__(self):
        return 'relationship from %s to %s' % (self.from_user.myuser.first_name, self.to_user.myuser.first_name)




# Create your models here.
