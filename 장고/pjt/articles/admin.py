from django.contrib import admin
from .models import Article
# 현재 디렉토리에 있는 model 에서 Article 불러옴

# Register your models here.
admin.site.register(Article)
