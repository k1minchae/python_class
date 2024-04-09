from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    subscribed_users = models.ManyToManyField(User, related_name='subscribed_user')

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.TextField()