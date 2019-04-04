from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

#clases
class personaForm(forms.Form):
	Nombre= forms.CharField(max_length=30)
	Apellido_Paterno= forms.CharField(max_length=25)
	Apellido_Materno = forms.CharField(max_length=25)
	Edad = forms.IntegerField()

	def clean(self):
		cleaned_data = super(personaForm, self).clean()
		Nombre = cleaned_data.get('Nombre')
		Apellido_Paterno = cleaned_data.get('Apellido_Paterno')
		Apellido_Materno = cleaned_data.get('Apellido_Materno')
		Edad = cleaned_data.get('Edad')
        

class trabajoForm(forms.Form):
	Nombre_trabajo= forms.CharField(max_length=30)
	Tipo_trabajo= forms.CharField(max_length=25)
	Salario = forms.IntegerField()

	def clean(self):
		cleaned_data = super(personaForm, self).clean()
		Nombre_trabajo = cleaned_data.get('Nombre_trabajo')
		Tipo_trabajo = cleaned_data.get('Tipo_trabajo')
		Salario = cleaned_data.get('Salario')
		
        

class carroForm(forms.Form):
	Nombre_carro= forms.CharField(max_length=30)
	Modelo= forms.CharField(max_length=25)
	Costo = forms.IntegerField()
	def clean(self):
		cleaned_data = super(personaForm, self).clean()
		Nombre_carro = cleaned_data.get('Nombre_carro')
		Modelo = cleaned_data.get('Modelo')
		Costo = cleaned_data.get('Costo')
		
class pasatiempoForm(forms.Form):
	Nombre_pasatiempo= forms.CharField(max_length=30)
	Tiempo = forms.IntegerField()

	def clean(self):
		cleaned_data = super(personaForm, self).clean()
		Nombre_pasatiempo = cleaned_data.get('Nombre_pasatiempo')
		Tiempo = cleaned_data.get('Tiempo')
		
        

class comidaForm(forms.Form):
	Nombre_comida= forms.CharField(max_length=30)
	Tipo_de_comida= forms.CharField(max_length=25)


	def clean(self):
		cleaned_data = super(personaForm, self).clean()
		Nombre_comida = cleaned_data.get('Nombre_comida')
		Tipo_de_comida = cleaned_data.get('Tipo_de_comida')

       