from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '비공개 게시글'
                }
            ),
            
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '비공개 게시글입니다.'
                }
            ),
            'image_description': forms.Textarea(
                attrs= {
                    'class': 'form-control',
                    'placeholder': '이미지는 없습니다.'
                },
            )

    }