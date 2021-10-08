from django import forms
from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    is_private = forms.BooleanField(required=False)
    class Meta:
        model = Project
        fields = ['name','image','description','is_private']
