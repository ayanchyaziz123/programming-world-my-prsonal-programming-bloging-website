from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm



class CommentForm(forms.ModelForm):

    email = forms.EmailField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control input-edit',
            'placeholder' : 'email'
        }
    ))
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-edit',
            'placeholder': 'name'
        }
    ))
    body = forms.CharField( widget=forms.Textarea(
        attrs={
            'class': 'form-control input-edit',
        }
    ))


    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')