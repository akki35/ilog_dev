from django.db import models
from django.template.defaultfilters import slugify
from django.db.models import signals


class Type(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Type'

    def __str__(self):
        return self.name

    # @models.permalink
    # def get_absolute_url(self):
    #   return ()


class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Asset'

    def __str__(self):
        return self.name


class Operation(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'operation'

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Material'

    def __str__(self):
        return self.name


class EnterpriseManager(models.Manager):
    def create_enterprise(self, enterprise, types, assets, products, materials, operations):
        enterprise = self.model(enterprise=enterprise,)  # types=types, assets=assets, products=products,
                               # materials=materials, operations=operations,)
        enterprise.save()


class Enterprise(models.Model):
    enterprise = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    types = models.ManyToManyField(Type)
    products = models.ManyToManyField(Product, through='EnterpriseProduct')
    assets = models.ManyToManyField(Asset)
    operations = models.ManyToManyField(Operation)
    materials = models.ManyToManyField(Material)

    objects = EnterpriseManager()

    def __str__(self):
        return self.enterprise

    def save(self, *args, **kwargs):
        if not self.id:                  # Newly created object, so set slug
            self.slug = slugify(self.enterprise).__str__()
            super(Enterprise, self).save(*args, **kwargs)


    def create_enterprise(self, enterprise,):   # types, assets, products, materials, operations):
        enterprise = self.model(enterprise=enterprise,)  # types=types, assets=assets, products=products,
                               # materials=materials, operations=operations)
        enterprise.save()


class EnterpriseProduct(models.Model):
    product = models.ForeignKey(Product)
    enterprise = models.ForeignKey(Enterprise)
    product_image = models.ImageField(upload_to='images/products/main')
    # product_thumbnail = models.ImageField(upload_to='images/products/thumbnails')
    caption = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.product.name

    def get_product_image(self):
        default_image = 'images/products/main/default.png'
        if self.product_image:
            return self.product_image
        else:
            return default_image



    # def get_product_thumbnail(self):
    #     default = 'images/products/thumbnail/default.png'
    #     if self.product_thumbnail:
    #         return self.product_thumbnail
    #     else:
    #         return default







# Create your models here.
