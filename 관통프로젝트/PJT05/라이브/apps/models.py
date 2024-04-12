from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()

class Query(models.Model): # 정석은 M:N 이지만 오늘은 1:N
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    keyword = models.TextField()
