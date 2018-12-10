from django.db import models


class StoreManager(models.Manager):
    def calculate(self, form):
        total = form['quantity']
        cost = Store.objects.get(id=form['product_id'])
        price = float(total)*float(cost.price)
        return price


class Store(models.Model):
    item = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = StoreManager()


    def __str__(self):
        items = f'{self.item} for ${self.price} each.'
        return items