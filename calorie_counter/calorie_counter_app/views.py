from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *

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
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

def home(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')


def editProfile(request):
    try:
        profile_info = UserProfileModel.objects.get(user=request.user)
    except UserProfileModel.DoesNotExist:
        profile_info = UserProfileModel(user=request.user)  # Create new profile if needed

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile_info)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = UserProfileForm(instance=profile_info)

    return render(request, 'editProfile.html', {'profile_form': profile_form})


