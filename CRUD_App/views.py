from django.shortcuts import render, redirect
from .forms import AlumnoForm
from .models import Alumnos

def index(request):
    return render(request, 'index.html')

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página principal después de agregar el alumno
    else:
        form = AlumnoForm()
    return render(request, 'agregar_alumno.html', {'form': form})

def eliminar_alumno(request):
    alumnos = Alumnos.objects.all()
    data = {'al': alumnos}
    return render (request, 'eliminar_alumno.html', data)