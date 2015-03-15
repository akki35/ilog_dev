from django.db import models
from enterprise.models import Enterprise
# from nodes.models import Node
from accounts.models import MyUser
from django.db.models.signals import post_save
from django.db.models import signals


class EnterpriseProfile(models.Model):
    enterprise = models.OneToOneField(Enterprise)
    address = models. CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=30, blank=True, null=True)
    website = models.URLField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='enterprise/main')

    def __str__(self):
        return self.enterprise

    def get_users(self):
        return self.enterprise.myuser_set.all()

    def get_products(self):
        return self.enterprise.products.all()

    def get_assets(self):
        return self.enterprise.assets.all()

    def get_enterprise_name(self):
        return self.enterprise.name

    # def get_nodes(self):
    #     a = self.enterprise.myuser.all()
    #     for ab in a:
    #         c = ab.node_set.all()
    #     return c

    def get_image(self):
        default = 'images/enterprise/main/enterprise.png'
        if self.image:
            return self.image
        else:
            return default


# def save(self, *args, **kwargs):
#         # if not self.id:                  # Newly created object, so set slug
#         #     self.slug = slugify(self.enterprise).__str__()
#     super(EnterpriseProfile, self).save(*args, **kwargs)


def create_enterprise_profile(sender, instance, created, **kwargs):
    """Create ModelB for every new ModelA."""
    if created:
        EnterpriseProfile.objects.create(enterprise=instance)

signals.post_save.connect(create_enterprise_profile, sender=Enterprise, weak=False,
                          dispatch_uid='models.create_enterprise_profile')

# post_save.connect(create_enterprise_profile, sender=MyUser)
# post_save.connect(save_enterprise_profile, sender=MyUser)


# Create your models here.

# def create_enterprise_profile()