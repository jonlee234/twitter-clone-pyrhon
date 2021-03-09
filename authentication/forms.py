from django import forms
from twitteruser.models import TwitterUser


class UserForm(forms.Form):
    name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)
