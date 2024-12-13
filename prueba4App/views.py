from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import Cliente
from django.contrib.auth.decorators import user_passes_test

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


def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        fecha_ingreso = request.POST['fecha_ingreso']
        Cliente.objects.create(nombre=nombre, telefono=telefono, fecha_ingreso=fecha_ingreso)
        return redirect('admin_page')
    return render(request, 'admin.html')


def admin_listado_clientes(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('login') 
    clientes = Cliente.objects.all()  
    return render(request, 'admin_listado.html', {'clientes': clientes})


def admin_buscar(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('login') 
    search = request.GET.get('search', '')
    clientes = []
    if search:
        clientes = Cliente.objects.filter(nombre__icontains=search) | Cliente.objects.filter(id__icontains=search)
    return render(request, 'admin_buscar.html', {'clientes': clientes, 'search': search})