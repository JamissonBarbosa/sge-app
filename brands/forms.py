from django import forms
from . import models

class Brandform(forms.ModelForm):
    model = models.Brand
    fields = ['name', 'description']