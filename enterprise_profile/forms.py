from django import forms
from enterprise_profile.models import EnterpriseProfile


class EnterpriseProfileForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea, max_length=200, required=False)
    contact = forms.CharField(widget=forms.Textarea, max_length=50, required=False)
    about = forms.CharField(widget=forms.Textarea, max_length=5000, required=False)
    capabilities = forms.CharField(widget=forms.Textarea, max_length=5000, required=False)
    people_detail = forms.CharField(widget=forms.Textarea, max_length=5000, required=False)
    product_intro = forms.CharField(widget=forms.Textarea, max_length=5000, required=False)
    website = forms.CharField(required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = EnterpriseProfile
        exclude = ['enterprise']
        fields = ['address', 'contact', 'about', 'website', 'image', 'capabilities', 'people_detail', 'product_intro']

