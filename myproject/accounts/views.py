from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

# Landing/login page
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('private')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

# Public page
def public_page(request):
    return render(request, 'accounts/public.html')

# Private page (restricted to logged-in users)
@login_required
def private_page(request):
    return render(request, 'accounts/private.html')

# User registration/profile creation
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            User.objects.create_user(username=username, password=password, email=email)
            return redirect('login')
        except:
            return render(request, 'accounts/register.html', {'error': 'User creation failed'})
    return render(request, 'accounts/register.html')

# Logout functionality
def logout_view(request):
    logout(request)
    return redirect('login')
