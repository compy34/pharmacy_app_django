from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'category', 'display_prescription_required')
    search_fields = ('name', 'manufacturer',)
    list_filter = ('category', 'prescription_required')

    @admin.display(boolean=True, description='Рецепт')
    def display_prescription_required(self, obj):
        # Якщо в базі лежить рядок 'True'/'False' або будь-що інше,
        # приводимо його до реального логічного типу bool
        val = obj.prescription_required
        if isinstance(val, str):
            return val.lower() == 'true'
        return bool(val)