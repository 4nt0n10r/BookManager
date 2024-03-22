from django import forms
from applications.login.forms import CustomSelect
from django.forms import ModelForm
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'gender']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': CustomSelect(),
            'gender': CustomSelect(),
        }
    