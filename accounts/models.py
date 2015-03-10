from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from enterprise.models import Enterprise
from django.template.defaultfilters import slugify


class MyUserManager(BaseUserManager):
    def create_myuser(self, email, first_name, last_name, enterprise, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError("must have a first_name")
        if enterprise not in Enterprise.objects.all():
            raise ValueError("please specify a valid enterprise or register a new one")

        user = self.model(email=self.normalize_email(email), first_name=first_name,
                          last_name=last_name, enterprise=enterprise,)

        user.set_password(password)
        user.save(using=self._db)

        print("user saved")

        return user

    def create_superuser(self, email, first_name, last_name, enterprise, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError("must have a first_name")
        if enterprise not in Enterprise.objects.all():
            raise ValueError("please specify a valid enterprise or register a new one")

        user = self.model(email=self.normalize_email(email), first_name=first_name,
                          last_name=last_name, enterprise=enterprise,)
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    # username = models.CharField(max_length=20, unique=True, db_index=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=False)
    email = models.EmailField(verbose_name='email address',
                              max_length=255, unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    enterprise = models.ForeignKey(Enterprise)  # import model

    objects = MyUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['enterprise', 'first_name', 'last_name']

    def __unicode__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        if not self.id:                  # Newly created object, so set slug
            self.slug = slugify(self.get_full_name()).__str__()
            super(MyUser, self).save(*args, **kwargs)


    # def create_myuser(self, email, first_name, last_name, enterprise, password=None):
    #     if not email:
    #         raise ValueError('Users must have an email address')
    #     if not first_name:
    #         raise ValueError("must have a first_name")
    #     if enterprise not in Enterprise.objects.all():
    #         raise ValueError("please specify a valid enterprise or register a new one")
    #
    #     myuser = self.model(email=self.normalize_email(email), first_name=first_name,
    #                         last_name=last_name, enterprise=enterprise,)
    #
    #     myuser.set_password(password)
    #     myuser.save(using=self._db)
    #     return myuser

# Create your models here.
