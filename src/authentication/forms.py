from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        label=False,
        widget=forms.TextInput(
            attrs={
                'class': 'textarea login__textarea',
                'placeholder': 'Pseudo'
            }
        )
    )
    password = forms.CharField(
        max_length=63,
        label=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'textarea login__textarea',
                'placeholder': 'Mot de passe'
            }
        )
    )


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username']
