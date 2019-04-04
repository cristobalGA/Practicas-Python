from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

#clases
class personaForm(forms.ModelForm):
	class Meta:
		model = persona
		fields = ('Nombre', 'Apellido_Paterno', 'Apellido_Materno')

class trabajoForm(forms.ModelForm):
	class Meta:
		model = trabajo
		fields = ('Nombre_trabajo', 'Tipo_trabajo','Salario')

class carroForm(forms.ModelForm):
	class Meta:
		model = carro
		fields = ('Nombre_carro', 'Modelo', 'Costo')

class pasatiempoForm(forms.ModelForm):
	class Meta:
		model = pasatiempo
		fields = ('Nombre_pasatiempo', 'Tiempo')

class comidaForm(forms.ModelForm):
	class Meta:
		model = comida
		fields = ('Nombre_comida', 'Tipo_de_comida')