# forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'phone_number', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Write your message...', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Full Name*', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email*', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
        }
