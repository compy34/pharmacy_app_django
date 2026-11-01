from django.db.models import Q
from django.shortcuts import render
from .models import Medicine



def home_view(request):
    return render(request, 'medicines/home.html')

def about_view(request):
    return render(request, 'medicines/about.html')


def list_view(request):
    query = request.GET.get('q', '')
    medicines=Medicine.objects.all()

    if query:
        medicines = medicines.filter(Q(name__icontains=query) | Q(manufaturer__icontains=query))

    context = {
        'medicines': medicines,
        'query': query,
    }
    return render(request, 'medicines/list.html', context)
