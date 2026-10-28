from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'castomer_name', 'created_at', 'status')
    list_filer = ('status', 'created_at')
    inlines = [OrderItemInline]
