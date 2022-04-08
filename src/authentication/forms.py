from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        label=False,
        widget=forms.TextInput(
            attrs={
                'class': 'textbox login__textarea',
                'placeholder': 'Pseudo'
            }
        )
    )
    password = forms.CharField(
        max_length=63,
        label=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'textbox login__textarea',
                'placeholder': 'Mot de passe'
            }
        )
    )


class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'textbox signup-textarea',
                'placeholder': "Mot de passe"
            }
        )
    )

    password2 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'textbox signup-textarea',
                'placeholder': "Confirmer mot de passe"
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'textbox signup-textarea',
                    'placeholder': "Nom d'utilisateur"
                }
            ),
        }
