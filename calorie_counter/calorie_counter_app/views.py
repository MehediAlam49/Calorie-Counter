from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register_view(request):
    
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return redirect('login_view')

def dashboard(request):
    return render(request, 'home.html')