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

def editar_alumno(request):
    if request.method == 'POST':
        alumno_id = request.POST.get('id')
        alumno = Alumnos.objects.get(id=alumno_id)

        # Actualiza los datos
        alumno.nombre = request.POST.get('nombre')
        alumno.carrera = request.POST.get('carrera')
        alumno.nota1 = request.POST.get('nota1')
        alumno.nota2 = request.POST.get('nota2')
        alumno.nota3 = request.POST.get('nota3')
        alumno.fecha_ingreso = request.POST.get('fecha_ingreso')
        alumno.save()

        # Redirige a la misma página después de guardar los cambios
        return redirect('editar_alumno')

    alumnos = Alumnos.objects.all()
    return render(request, 'editar_alumno.html', {'al': alumnos})