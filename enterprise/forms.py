from django import forms
from django.core.exceptions import ValidationError
from enterprise.models import *


def unique_enterprise_validator(value):
    if Enterprise.objects.filter(enterprise__iexact=value).exists():
        raise ValidationError("This enterprise already exists")


class EnterpriseRegistrationForm(forms.ModelForm):
    enterprise = forms.CharField(max_length=255)
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=False)
    assets = forms.ModelMultipleChoiceField(queryset=Asset.objects.all(), required=False)
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False)
    materials = forms.ModelMultipleChoiceField(queryset=Material.objects.all(), required=False)
    operations = forms.ModelMultipleChoiceField(queryset=Operation.objects.all(), required=False)

    class Meta:
        model = Enterprise
        exclude = ['slug']
        fields = ['enterprise', 'types', 'assets', 'products', 'materials', 'operations',]

    def __init__(self, *args, **kwargs):
        super(EnterpriseRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['enterprise'].validators.append(unique_enterprise_validator)



