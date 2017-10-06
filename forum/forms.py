from django import forms
from .models import *


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('subject',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
