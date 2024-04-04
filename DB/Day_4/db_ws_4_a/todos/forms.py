from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('work', 'is_completed', 'content',)
        widgets = {'is_completed': forms.HiddenInput()}