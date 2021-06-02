from django import forms
from django.forms import fields
from blog.models import Coment, Post

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'md-textarea form-control',
        'rows': '4',
    }))
    class Meta:
        model = Coment
        fields = {'content',}

class PostForm(forms.ModelForm):
    class Meta :
        model = Post
        fields = "__all__"