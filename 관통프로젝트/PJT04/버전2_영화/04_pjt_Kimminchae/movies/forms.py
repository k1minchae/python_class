from .models import Movie, Comment
from django import forms

class CreateMovie(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)