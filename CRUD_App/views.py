from django.shortcuts import render, redirect
from .forms import AlumnoForm
from .models import Alumnos

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_alumno')
    else:
        form = AlumnoForm()
    return render(request, 'agregar_alumno.html', {'form': form})

def eliminar_alumno(request):
    alumnos = Alumnos.objects.all()
    data = {'al': alumnos}
    if request.method == 'POST':
        alumno_id = request.POST.get('alumno_id')
        if alumno_id:
            try:
                alumno = Alumnos.objects.get(id=alumno_id)
                alumno.delete()
            except Alumnos.DoesNotExist:
                pass 
            return redirect('eliminar_alumno') 
    return render (request, 'eliminar_alumno.html', data)

def editar_alumno(request):
    if request.method == 'POST':
        alumno_id = request.POST.get('id')
        alumno = Alumnos.objects.get(id=alumno_id)

        alumno.nombre = request.POST.get('nombre')
        alumno.carrera = request.POST.get('carrera')
        alumno.nota1 = request.POST.get('nota1')
        alumno.nota2 = request.POST.get('nota2')
        alumno.nota3 = request.POST.get('nota3')
        alumno.fecha_ingreso = request.POST.get('fecha_ingreso')
        alumno.save()

        return redirect('editar_alumno')

    alumnos = Alumnos.objects.all()
    return render(request, 'editar_alumno.html', {'al': alumnos})

def buscar_alumno(request):
    query = request.GET.get('q', '') 
    if query:
        alumnos = Alumnos.objects.filter(nombre__icontains=query)  
    else:
        alumnos = Alumnos.objects.all() 

    return render(request, 'buscar_alumno.html', {'alumnos': alumnos})