from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 20)
    content = models.CharField(max_length = 20)
    image = models.ImageField(blank=True)
    image_description = models.TextField()
    is_public = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add =True)

