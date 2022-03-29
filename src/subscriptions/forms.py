from django import forms


class SubscriptionsForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        label='Suivre un utilisateur'
    )
