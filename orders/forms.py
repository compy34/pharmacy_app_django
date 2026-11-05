from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'castomer_name', 'phone', 'delivery_adress'
        ]
        labels = {
            'castomer_name': 'Customer Name',
            'phone': 'Phone Number',
            'delivery_adress': 'Delivery Address'
        }
        widgets = {
            'castomer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_adress': forms.TextInput(attrs={'class': 'form-control'}),
        }