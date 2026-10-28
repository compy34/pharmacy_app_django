from django.db import models
from django.conf import settings
from pharmacies.models import PharmacyMedicine

class Order(models.Model):
    STATUS_CHOICES = [
    ('new', 'New'),
    ('confirmed', 'Confirmed'),
    ('delivery', 'Delivery'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    castomer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    delivery_adress = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f'order #{self.pk}'

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    pharmacy_medicine = models.ForeignKey(PharmacyMedicine, on_delete=models.PROTECT, related_name='items')
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    @property
    def total_price(self):
        return self.quantity * self.price


