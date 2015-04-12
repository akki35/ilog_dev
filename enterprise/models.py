from django.db import models
from django.template.defaultfilters import slugify
from django.db.models import signals
from ilog_dev.unique_slug import unique_slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Type(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Type'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:                  # Newly created object, so set slug
            self.slug = slugify(self.name).__str__()
            super(Type, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:                  # Newly created object, so set slug
            self.slug = slugify(self.name).__str__()
            super(Product, self).save(*args, **kwargs)


class Asset(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Asset'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:                  # Newly created object, so set slug
            self.slug = slugify(self.name).__str__()
            super(Asset, self).save(*args, **kwargs)


class Operation(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'operation'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:                  # Newly created object, so set slug
            self.slug = slugify(self.name).__str__()
            super(Operation, self).save(*args, **kwargs)


class Material(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Material'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:                  # Newly created object, so set slug
            self.slug = slugify(self.name).__str__()
            super(Material, self).save(*args, **kwargs)


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
    assets = models.ManyToManyField(Asset, through='EnterpriseAsset')
    operations = models.ManyToManyField(Operation)
    materials = models.ManyToManyField(Material)

    objects = EnterpriseManager()

    def __str__(self):
        return self.enterprise

    def save(self, *args, **kwargs):
        if not self.id:                  # Newly created object, so set slug
            slug_str = self.enterprise
            unique_slugify(self, slug_str)
            # self.slug = slugify(self.enterprise).__str__()
            super(Enterprise, self).save(*args, **kwargs)


    def create_enterprise(self, enterprise,):   # types, assets, products, materials, operations):
        enterprise = self.model(enterprise=enterprise,)  # types=types, assets=assets, products=products,
                               # materials=materials, operations=operations)
        enterprise.save()


class EnterpriseProduct(models.Model):
    product = models.ForeignKey(Product)
    enterprise = models.ForeignKey(Enterprise)
    product_image = ProcessedImageField(upload_to='products/main',
                                        processors=[ResizeToFill(1000, 1000)],
                                        format='JPEG',
                                        options={'quality': 60})
    product_image_thumbnail = ProcessedImageField(upload_to='products/thumbnails',
                                                  processors=[ResizeToFill(100, 100)],
                                                  format='JPEG',
                                                  options={'quality': 60})
    caption = models.CharField(max_length=200, default='product')
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.product.name

    def get_product_image(self):
        default_image = 'products/main/product.jpg'
        if self.product_image:
            return self.product_image
        else:
            return default_image

    def get_product_image_thumbnail(self):
        default = 'products/thumbnails/enterprise.jpg'
        if self.product_image_thumbnail:
            return self.product_image_thumbnail
        else:
            return default


class EnterpriseAsset(models.Model):
    asset = models.ForeignKey(Asset)
    enterprise = models.ForeignKey(Enterprise)
    asset_image = ProcessedImageField(upload_to='assets/main',
                                        processors=[ResizeToFill(300, 300)],
                                        format='JPEG',
                                        options={'quality': 60})
    asset_image_thumbnail = ProcessedImageField(upload_to='assets/thumbnails',
                                                  processors=[ResizeToFill(100, 100)],
                                                  format='JPEG',
                                                  options={'quality': 60})
    caption = models.CharField(max_length=200, default='product')
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.asset.name

    def get_asset_image(self):
        default_image = 'assets/main/asset.jpg'
        if self.asset_image:
            return self.asset_image
        else:
            return default_image

    def get_asset_image_thumbnail(self):
        default = 'assets/thumbnails/asset.jpg'
        if self.asset_image_thumbnail:
            return self.asset_image_thumbnail
        else:
            return default


# Create your models here.
