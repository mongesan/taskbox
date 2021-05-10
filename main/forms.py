from django import forms
from django.forms import ModelForm
from main.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'comment', 'stat_max', 'deadline')

        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
            'stat_max': forms.NumberInput(attrs={'min': 1, 'max': 100}),
            'deadline': forms.DateInput(attrs={"type": "date"})
        }


class TaskFormEdit(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'deadline')
        widgets = {
            'deadline': forms.DateInput(attrs={"type": "date"})
        }
