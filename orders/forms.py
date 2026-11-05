from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields =[
            'castomer_name', 'phone', 'delivery_address'
        ]
        labels = {
            'castomer_name': 'Castomer Name',
            'phone': 'Phone Number',
            'delivery_address': 'Delivery Address'
        }
        widgets = {
            'castomer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-control'}),
        }