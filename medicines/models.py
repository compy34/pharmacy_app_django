from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=200, verbose_name="Medicine")
    manufacturer = models.CharField(max_length=200, verbose_name="Manufacturer")
    description = models.TextField(verbose_name="Description")