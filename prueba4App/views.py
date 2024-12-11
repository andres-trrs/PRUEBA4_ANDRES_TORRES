from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect('admin_page') 
            else:
                return redirect('user_page')  
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    
    return render(request, 'login.html')

def admin_page(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('login')  
    return render(request, 'admin.html')

def user_page(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    return render(request, 'user.html')