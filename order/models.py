from django.db import models
from django.contrib.auth.models import User

from product.models import Product
# Create your models here.

class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    STATUS_CHOICES = (
        (ORDERED, 'ordered'),
        (SHIPPED, 'shipped')
    )
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    place = models.CharField(max_length=255)

    created_at=models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=True)
    paid_amount=models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=ORDERED)


    def __str__(self):
        return self.status

    class Meta:
        ordering = ('-created_at',)


    def get_total_price(self):
       pass

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity= models.IntegerField(default=1)

    def __str__(self):
        return self.order.status


    def get_total_price(self):
        return self.price
