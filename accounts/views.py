from django.contrib.auth import login
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm


def signup_view(request):
    if request.user.is_authenticated:
         return redirect('home')


    # 2
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'accounts/signup.html', context={
            'form': form
        })

    # 3
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, "accounts/signup.html")

def signin_view(request):
    return render(request, "accounts/signin.html")

def signout_view(request):
    return render(request, "accounts/signout.html")

def profile_view(request):
    return render(request, "accounts/profile.html")


