from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from enterprise.models import Enterprise
from django.template.defaultfilters import slugify
# from slug-u import unique_slugify
import re
# from django.template.defaultfilters import slugify


def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    """
    Calculates and stores a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len-len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value


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
    slug = models.SlugField(max_length=255, unique=True)
    email = models.EmailField(verbose_name='email address',
                              max_length=255, unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    enterprise = models.ForeignKey(Enterprise)  # import model

    objects = MyUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'enterprise']

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
            slug_str = self.get_full_name()
            unique_slugify(self, slug_str)
            # self.slug = slugify(self.get_full_name()).__str__()
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
