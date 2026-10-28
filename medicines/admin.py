from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'category', 'prescription_required')
    search_fields = ('name', 'manufacturer',)
    list_filter = ('category', 'prescription_required')