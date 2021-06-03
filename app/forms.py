from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Mamography


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
class MamographyForm(forms.ModelForm):
    class Meta:
        model = Mamography
        fields = (
            'imagen',
            )


