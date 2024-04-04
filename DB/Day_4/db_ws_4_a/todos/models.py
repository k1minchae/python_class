from django.db import models
from accounts.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    work = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)