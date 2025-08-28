from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user_exists = CustomUserModel.objects.filter(username = username).exists()
        if user_exists:
            return redirect('register_view')
        else:
            if password == confirm_password:
                user = CustomUserModel.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )

                if user:
                    UserProfileModel.objects.create(
                        user=user,
                    )
                    return redirect('login_view')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

def home(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')