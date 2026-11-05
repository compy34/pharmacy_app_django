from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Medicine
from pharmacies.models import PharmacyMedicine


def home_view(request):
    return render(request, 'medicines/home.html')

def about_view(request):
    return render(request, 'medicines/about.html')


def list_view(request):
    query = request.GET.get('q', '')
    medicines=Medicine.objects.all()

    if query:
        medicines = medicines.filter(Q(name__icontains=query) | Q( manufacturer__icontains=query))

    context = {
        'medicines': medicines,
        'query': query,
    }
    return render(request, 'medicines/list.html', context)


def details_view(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)

    offers = PharmacyMedicine.objects.filter(medicine=medicine, quantity__gt=0).select_related('pharmacy').order_by('price')
    context = {
        'medicine': medicine,
        'offers': offers,
    }
    return render(request, 'medicines/details.html', context)
