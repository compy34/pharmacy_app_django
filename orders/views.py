from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from pharmacies.models import PharmacyMedicine
from django.contrib import messages
from .forms import OrderForm
from .models import OrderItem

def add_to_cart(request, offer_id):
    offer = get_object_or_404(PharmacyMedicine, id=offer_id, quantity__gt=0)
    cart = request.session.get('cart', {})
    key = str(offer_id)
    if key in cart:
        cart[key] += 1
    else:
        cart[key] = 1

    request.session['cart'] = cart
    return redirect('cart')


def cart_view(request):
    cart = request.session.get('cart', {})

    offers = PharmacyMedicine.objects.filter(id__in=cart.keys()).select_related('medicine', 'pharmacy')
    items = []
    total = 0
    for offer in offers:
        quantity = cart[str(offer.id)]
        item_total = (offer.price * quantity)
        total += item_total
        items.append(
            {
                'offer' : offer,
                'quantity' : quantity,
                'total' : item_total,

            }
        )
    return render(request, 'orders/cart.html', context={'items': items, 'total': total})
# Create your views here.


@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')

    offers = PharmacyMedicine.objects.filter(id__in=cart.keys())

    if request.method == 'GET':
        form = OrderForm(initial={
            'castomer_name': request.user.get_full_name() or request.user.username,
            'phone': ''
        })

    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)

            order.user = request.user
            order.save()

            for offer in offers:
                quantity = cart[str(offer.id)]

                OrderItem.objects.create(order=order,pharmacy_medicine=offer, quantity=quantity, price=offer.price)

            request.session['cart'] = {}
            messages.success(request, 'Thank you for your order!')

            return redirect('my_orders')


    return render(request, 'orders/checkout.html', context={'form': form})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def my_orders(request):
    orders = (request.user.orders.prefetch_related(
        'items__pharmacy_medicine__medicine',
        'items__pharmacy_medicine__pharmacy',
    )).order_by('-created_at')

    return render(request, 'orders/my_orders.html', context={'orders': orders})