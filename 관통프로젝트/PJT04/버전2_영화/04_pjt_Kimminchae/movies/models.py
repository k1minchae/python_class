from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
class Movie(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True)


    COMEDY = 'Comedy'
    FANTASY = 'Fantasy'
    ROMANCE = 'Romance'

    GENRE_CHOICES = [
        (COMEDY, 'Comedy'),
        (FANTASY, 'Fantasy'),
        (ROMANCE, 'Romance'),
    ]
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, default=COMEDY)
    score = models.DecimalField(max_digits=2, decimal_places=1, default=0.0, choices=[(i / 2, i / 2) for i in range(11)])

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.CharField(max_length = 250)
    