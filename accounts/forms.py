from django import forms
from django.core.exceptions import ValidationError
from accounts.models import MyUser
from enterprise.models import Enterprise


def unique_email_validator(value):
    if MyUser.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')


class SignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    enterprise = forms.ModelChoiceField(queryset=Enterprise.objects.all(),
                                        help_text="Choose from existing"
                                        " if company already registered "
                                        "or register now!")
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                       label="Confirm your password",
                                       required=True)

    class Meta:
        model = MyUser
        exclude = ['joined', 'is_active', 'is_admin', 'slug']
        fields = ['email', 'enterprise', 'first_name', 'last_name', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].validators.append(unique_email_validator)

    def clean(self):
        super(SignupForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(['Passwords don\'t match'])
        return self.cleaned_data


# class LoginForm(forms.ModelForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))