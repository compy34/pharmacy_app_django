from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=200, verbose_name="Medicine")
    manufacturer = models.CharField(max_length=200, verbose_name="Manufacturer")
    description = models.TextField(verbose_name="Description")
    category = models.CharField(max_length=200, verbose_name="Category")
    prescription_required = models.TextField(default= False,verbose_name="Prescription")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Medicine"
        verbose_name_plural = "Medicines"
        ordering = ['name']
