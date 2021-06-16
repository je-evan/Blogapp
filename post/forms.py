from django.forms import widgets
from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)
    
        widgets = {
            'message': forms.Textarea(
                attrs={
                    'id': "exampleFormControlTextarea1",
                    'rows': 3
                    }
                ),
            }