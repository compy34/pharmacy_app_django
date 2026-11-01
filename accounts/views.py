from django.shortcuts import render

def signup_view(request):
    return render(request, "accounts/signup.html")

def signin_view(request):
    return render(request, "accounts/signin.html")

def signout_view(request):
    return render(request, "accounts/signout.html")

def profile_view(request):
    return render(request, "accounts/profile.html")


