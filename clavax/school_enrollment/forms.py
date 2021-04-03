from django import forms
from django.core import validators
#from . models import *
from .models import Student
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    class Meta():
        model=Student
        fields ='__all__'
        


