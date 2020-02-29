from django import forms
from .models import Task

class TaskForm(forms.Form):
    note = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Create Task'}))


    class Meta:
        model = Task
        fields = ('note',)
       
   
   
    

