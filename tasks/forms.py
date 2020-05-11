from django.forms import ModelForm
from django import forms

from .models import *


# this is the form we are creating to get data 

class taskForms(forms.ModelForm):

    class Meta:
        # model that we are teing to creat the form for
        model = task

        # fields required 
        fields = '__all__'
