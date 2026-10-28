from django.contrib import admin
from .models import Pharmacy, PharmacyMedicine


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone' )
    search_fields = ('name','address')


@admin.register(PharmacyMedicine)
class PharmacyMedicineAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'pharmacy', 'price', 'quantity' )
    search_fields = ('medicine__name', 'pharmacy__name')
    list_filter = ('pharmacy',)
