from django import forms
from django.core.exceptions import ValidationError
from enterprise.models import *


def unique_enterprise_validator(value):
    if Enterprise.objects.filter(enterprise__iexact=value).exists():
        raise ValidationError("This enterprise already exists")


class EnterpriseRegistrationForm(forms.ModelForm):
    enterprise = forms.CharField(max_length=255, help_text='If you give a name like "Abc Enterprises, you will get a url'
                                                           ' like www.industrylogger.com/enterprises/abc-enterprises')
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=False,
                                           help_text='Select one or more  Use Ctrl to select more than one')
    # assets = forms.ModelMultipleChoiceField(queryset=Asset.objects.all(), required=False)
    # products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False)
    materials = forms.ModelMultipleChoiceField(queryset=Material.objects.all(), required=False,
                                               help_text='Select one or more  Use Ctrl to select more than one')
    operations = forms.ModelMultipleChoiceField(queryset=Operation.objects.all(), required=False)


    class Meta:
        model = Enterprise
        exclude = ['slug', 'products', 'assets',]
        fields = ['enterprise', 'types', 'materials', 'operations', ]

    def __init__(self, *args, **kwargs):
        super(EnterpriseRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['enterprise'].validators.append(unique_enterprise_validator)


class ProductForm(forms.ModelForm):
    prod = forms.CharField()
    description = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
    product_image = forms.ImageField(required=False)
    caption = forms.CharField(max_length=255, required=False)

    class Meta:
        model = EnterpriseProduct
        exclude = ['enterprise', 'status']
        fields = ['prod', 'product_image', 'description', 'caption']


class AssetForm(forms.ModelForm):
    asse = forms.CharField()
    description = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
    asset_image = forms.ImageField(required=False)
    caption = forms.CharField(max_length=255, required=False)

    class Meta:
        model = EnterpriseAsset
        exclude = ['enterprise', 'status']
        fields = ['asse', 'asset_image', 'description', 'caption']


class TypeForm(forms.ModelForm):
    name = forms.CharField(max_length=25)

    class Meta:
        model = Type
        exclude = ['slug', 'is_active']
        fields = ['name']


class MaterialForm(forms.ModelForm):
    name = forms.CharField(max_length=25)

    class Meta:
        model = Material
        exclude = ['slug', 'is_active', ]
        fields = ['name']


class OperationForm(forms.ModelForm):
    name = forms.CharField(max_length=25)

    class Meta:
        model = Operation
        exclude = ['slug', 'is_active', ]
        fields = ['name']


