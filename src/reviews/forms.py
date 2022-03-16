from django import forms
from reviews import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = '__all__'
