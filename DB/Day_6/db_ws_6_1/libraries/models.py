from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    # subscribed_users = models.ManyToManyField(User, related_name='subscribed_user')
    def __str__(self):
        return self.nickname

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.TextField()
    def __str__(self):
        return self.title