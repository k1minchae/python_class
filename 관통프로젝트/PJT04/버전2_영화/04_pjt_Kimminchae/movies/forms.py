from .models import Movie, Comment
from django import forms

class CreateMovie(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ('user',)

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)