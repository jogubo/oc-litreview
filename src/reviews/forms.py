from django import forms
from reviews import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ('title', 'description', 'image')
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'image': 'Image'
        }
        widgets = {
            'title': forms.Textarea(
                attrs={
                    'class': 'textarea form-textarea form-textarea-title',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'textarea form-textarea form-textarea-description',
                }
            ),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ('rating', 'headline', 'body')
        labels = {
            'rating': 'Note',
            'headline': 'Titre',
            'body': 'Commentaire'
        }
        widgets = {
            'rating': forms.RadioSelect(
                choices=[
                    (0, '0'),
                    (1, '1'),
                    (2, '2'),
                    (3, '3'),
                    (4, '4'),
                    (5, '5'),
                ]
            ),
            'headline': forms.Textarea(
                attrs={
                    'class': 'textarea form-textarea form-textarea-title',
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'textarea form-textarea form-textarea-description',
                }
            ),
        }
