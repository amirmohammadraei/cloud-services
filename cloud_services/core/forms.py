from django import forms
from django.forms import fields
from .models import *


PHOTOS_CHOICES =(
    ("1", "photo1"),
    ("2", "photo2"),
    ("3", "photo3"),
    ("4", "photo4"),
    ("5", "photo5"),
)


class CommentForm(forms.ModelForm):
    photo = forms.ChoiceField(label='photo', choices=PHOTOS_CHOICES)

    class Meta:
        model = Comment
        fields = ('username', 'comment', 'photo')
        labels = {
            'username': 'username',
            'comment': 'comment',
        }
