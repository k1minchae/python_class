from django.db import models
from accounts.models import User

# Create your models here.
class Store(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    address = models.CharField(max_length = 100)
    is_franchise = models.BooleanField()

class Product(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    store = models.ForeignKey(Store, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    amount = models.IntegerField()
    price = models.IntegerField()
    adult = models.BooleanField()