from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True)

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.CharField(max_length = 250)
    