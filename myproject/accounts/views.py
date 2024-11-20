from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Profile
from django.contrib import messages
import os

# Create your views here.

# Landing/login page
def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('private')

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
    profiles = Profile.objects.all()  # Get all user profiles
    return render(request, 'accounts/public.html', {'profiles': profiles})

@login_required
def private_page(request):
    profile = request.user.profile

    if request.method == 'POST':
        if 'upload_image' in request.POST and request.FILES.get('image'):
            # Replace the current image with the uploaded one
            profile.image = request.FILES['image']
            profile.save()
        elif 'delete_image' in request.POST:
            # Delete the current image
            profile.image = None
            profile.save()
        return redirect('private')  # Reload the private page after upload or delete

    return render(request, 'accounts/private.html', {'profile': profile})


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


# Image upload
@login_required
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        request.user.profile.image = image
        request.user.profile.save()
        return redirect('private')
    return redirect('private')

# Image deletion
@login_required
def delete_image(request):
    if request.method == 'POST':
        profile = request.user.profile
        if profile.image:
            image_path = profile.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
            # Set the image field to None and save the profile
            profile.image = None
            profile.save()
        return redirect('private')