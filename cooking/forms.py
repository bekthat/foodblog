from django import forms
from .models import Posts

class PostAddForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'photo', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }