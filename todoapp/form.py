from django import forms
from .models import Task
class ToDoForms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','remarks','date']
