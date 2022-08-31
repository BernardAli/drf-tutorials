from decimal import Decimal

from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=49.99)

    @property
    def get_discount(self):
        return f"{round(float(self.price) * 0.2, 2)}"

    @property
    def sale_price(self):
        discounted_price = self.price - Decimal(self.get_discount)
        return discounted_price

    def __str__(self):
        return self.title
