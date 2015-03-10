from django.contrib import admin
from django import forms
from enterprise.models import *


# class TypeCreationForm(forms.ModelForm):

    # def save(self, commit=True):
        # Save the provided password in hashed format
        # type = super(TypeCreationForm, self).save(commit=False)

        # if commit:
        #    type.save()
        # return type
class TypeAdmin(admin.ModelAdmin):
    # form = TypeAdminForm

    list_display = ('name', 'slug')
    search_fields = ['name']
    ordering = ['name']

admin.site.register(Type, TypeAdmin)


class ProductAdmin(admin.ModelAdmin):
    # form = TypeAdminForm

    list_display = ('name', 'slug')
    search_fields = ['name']
    ordering = ['name']

admin.site.register(Product, ProductAdmin)


class AssetAdmin(admin.ModelAdmin):
    # form = TypeAdminForm

    list_display = ('name', 'slug')
    search_fields = ['name']
    ordering = ['name']

admin.site.register(Asset, AssetAdmin)


class OperationAdmin(admin.ModelAdmin):
    # form = TypeAdminForm

    list_display = ('name', 'slug')
    search_fields = ['name']
    ordering = ['name']

admin.site.register(Operation, OperationAdmin)


class MaterialAdmin(admin.ModelAdmin):
    # form = TypeAdminForm

    list_display = ('name', 'slug')
    search_fields = ['name']
    ordering = ['name']

admin.site.register(Material, MaterialAdmin)


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ['enterprise', 'slug']  # 'types', 'operations', 'assets',
                   # 'materials', 'products']
    fieldsets = (
        (None, {'fields': ('enterprise', 'slug')}),
        ('Categorization', {'fields': ('types', 'operations', 'assets',
                                       'materials', )}),    # products
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('enterprise', 'slug', 'types', 'operations', 'assets',
                       'materials', 'products')}
        ),
    )
    search_fields = ('enterprise',)
    ordering = ('enterprise',)

admin.site.register(Enterprise, EnterpriseAdmin)


class ProductCreationForm(forms.ModelForm):

    def save(self, commit=True):
        # Save the provided password in hashed format
        product = super(ProductCreationForm, self).save(commit=False)

        if commit:
            product.save()
        return product


class AssetCreationForm(forms.ModelForm):

    def save(self, commit=True):
        # Save the provided password in hashed format
        asset = super(AssetCreationForm, self).save(commit=False)

        if commit:
            asset.save()
        return asset


class OperationCreationForm(forms.ModelForm):

    def save(self, commit=True):
        # Save the provided password in hashed format
        operation = super(OperationCreationForm, self).save(commit=False)

        if commit:
            operation.save()
        return operation


class MaterialCreationForm(forms.ModelForm):

    def save(self, commit=True):
        # Save the provided password in hashed format
        material = super(MaterialCreationForm, self).save(commit=False)

        if commit:
            material.save()
        return material


class EnterpriseCreationForm(forms.ModelForm):

    def save(self, commit=True):
        # Save the provided password in hashed format
        enterprise = super(EnterpriseCreationForm, self).save(commit=False)

        if commit:
            enterprise.save()
        return enterprise

# Register your models here.
