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
    if request.method == 'POST':
        alumno_id = request.POST.get('alumno_id')
        if alumno_id:
            # Elimina el alumno de la base de datos
            try:
                alumno = Alumnos.objects.get(id=alumno_id)
                alumno.delete()
            except Alumnos.DoesNotExist:
                pass  # Si no existe el alumno, no hacemos nada (se podría agregar un mensaje de error)
            return redirect('eliminar_alumno') 
    return render (request, 'eliminar_alumno.html', data)