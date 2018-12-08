from django.db import models
from ..users.models import User

# Create your models here.

class StoreManager(models.Manager):
    # def calculate(self, form):
    #     print(form)
    pass

class Store(models.Model):
    item = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = StoreManager()


    def __str__(self):
        items = f'There are {self.quantity} {self.item} left at ${self.price} each.'
        return items