from django import forms
from reviews import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
