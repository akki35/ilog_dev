from django import forms
from myuserprofile.models import MyUserProfile


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    GenderChoices = (('M', 'Male'), ('F', 'Female'),)
    gender = forms.ChoiceField(choices=GenderChoices, widget=forms.Select(attrs={'class':'regDropDown'}))
    job_position = forms.CharField(max_length=255, required=False)
    experience = forms.CharField(widget=forms.Textarea, max_length=5000)
    summary = forms.CharField(widget=forms.Textarea, max_length=5000)

    class Meta:
        model = MyUserProfile
        exclude = ['follows', 'score', 'myuser']
        fields = ['image', 'gender', 'job_position', 'experience', 'summary']