from django import forms


class SubscriptionsForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        label=False,
        widget=forms.TextInput(
            attrs={
                'class': 'textbox',
                'placeholder': "Nom d'utilisateur"
            }
        )
    )
