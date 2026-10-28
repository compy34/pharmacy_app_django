from django.db import models
from medicines.models import Medicine

class Pharmacy(models.Model):
    name = models.CharField(max_length=100, verbose_name="Pharmacy Name")
    address = models.CharField(max_length=300, verbose_name="Pharmacy Address")
    phone = models.CharField(max_length=20, verbose_name="Phone Number")
    working_hours = models.CharField(max_length=100,blank=True, verbose_name="Working Hours")

    def __str__(self):
        return f"{self.name} - {self.address}"

    class Meta:
        verbose_name_plural = "Pharmacies"
        ordering = ['name']
        db_table = 'pharmacies'
        unique_together = (('name','address'),)


class PharmacyMedicine(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name='medicine_stock')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='pharmacy_stock')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Medicine Price")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity")

    def __str__(self):
        return f"{self.medicine.name} - {self.pharmacy.address}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['pharmacy', 'medicine'],
                name='unique_pharmacy_medicine'

            )
        ]


