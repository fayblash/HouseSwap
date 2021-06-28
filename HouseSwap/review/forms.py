from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        
    text = forms.CharField(label="Review", widget=forms.Textarea(attrs={'placeholder': 'Write a review...'}))