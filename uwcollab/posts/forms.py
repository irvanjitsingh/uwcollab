from django import forms
from django.contrib.auth.models import User


class PostForm(forms.Form):
    title = forms.CharField(required=True)
    content = forms.CharField(required=True)

    class Meta:
        model = User
