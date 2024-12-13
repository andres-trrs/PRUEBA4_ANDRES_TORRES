from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from .models import Cliente

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
    clientes = Cliente.objects.all() 
    return render(request, 'user.html', {'clientes': clientes})


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

def admin_eliminar(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('login')
    clientes = Cliente.objects.all() 
    if request.method == "POST":
        cliente_id = request.POST.get('cliente_id')
        if cliente_id:
            cliente = get_object_or_404(Cliente, id=cliente_id)
            cliente.delete()  
            return redirect('admin_eliminar')

    return render(request, 'admin_eliminar.html', {'clientes': clientes})

def user_buscar(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    search = request.GET.get('search', '')
    clientes = []
    if search:
        clientes = Cliente.objects.filter(nombre__icontains=search) | Cliente.objects.filter(id__icontains=search)
    return render(request, 'user_buscar.html', {'clientes': clientes, 'search': search})