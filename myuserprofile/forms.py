from django import forms
from myuserprofile.models import MyUserProfile
from enterprise.models import Operation


class ProfileForm(forms.ModelForm):
    image = forms.ImageField()
    GenderChoices = (('M', 'Male'), ('F', 'Female'),)
    gender = forms.ChoiceField(choices=GenderChoices, widget=forms.Select(attrs={'class':'regDropDown'}))
    job_position = forms.CharField(max_length=255, required=False)
    experience = forms.CharField(widget=forms.Textarea, max_length=5000, required=False)
    summary = forms.CharField(widget=forms.Textarea, max_length=5000, required=False)
    skillset = forms.ModelMultipleChoiceField(queryset=Operation.objects.all(), required=False)


    class Meta:
        model = MyUserProfile
        exclude = ['follows', 'score', 'myuser']
        fields = ['image', 'gender', 'job_position', 'experience', 'summary']