from django import forms
from django.utils.translation import ugettext_lazy as _


from .models import Comment, Topic

class CreateTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title', 'description'
        ]

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body'
        ]
      
    body = forms.CharField(label='Comments', widget=forms.Textarea(attrs={'placeholder': 'Enter new reply...'}))