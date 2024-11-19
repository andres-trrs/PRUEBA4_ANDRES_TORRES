from django import forms
from .models import Alumnos

class AlumnoForm(forms.ModelForm):
    CARRERA_CHOICES = [
        ('informatica', 'Informática'),
        ('administracion', 'Administración'),
        ('mecanica', 'Mecánica'),
        ('construccion', 'Construcción'),
    ]

    nombre = forms.CharField(
        label = 'Nombre',
        required = True,
    )

    nota1 = forms.FloatField(
        label = 'Nota 1',
        min_value = 1.0,
        max_value = 7.0,
        required = True,
    )

    nota2 = forms.FloatField(
        label = 'Nota 2',
        min_value = 1.0,
        max_value = 7.0,
        required = True,
    )

    nota3 = forms.FloatField(
        label = 'Nota 3',
        min_value = 1.0,
        max_value = 7.0,
        required = True,
    )

    carrera = forms.ChoiceField(choices=CARRERA_CHOICES, required=True)

    class Meta:
        model = Alumnos
        fields = ['nombre', 'nota1', 'nota2', 'nota3', 'fecha_ingreso', 'carrera']
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
        }