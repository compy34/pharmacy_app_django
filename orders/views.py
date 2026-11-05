from django.shortcuts import render, redirect, get_object_or_404
from pharmacies.models import PharmacyMedicine

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
