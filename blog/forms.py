from dataclasses import fields
from tkinter.tix import Form
from django import forms
from django import forms

from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content')