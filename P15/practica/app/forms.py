from django import forms
from .models import disquera, musico, disco, cancion, manager
from django.contrib.auth.forms import UserCreationForm

#clases
class disqueraForm(forms.Form):
    nombredisquera= forms.CharField(max_length=30)
    nodiscos= forms.IntegerField()
    ceo = forms.CharField(max_length=25)

    def clean(self):
        cleaned_data = super(disqueraForm, self).clean()
        nombredisquera = cleaned_data.get('nombredisquera')
        nodiscos = cleaned_data.get('nodiscos')
        ceo = cleaned_data.get('ceo')
        if not nombredisquera and not ceo:
            raise forms.ValidationError('Escribe algo!')

class managerForm(forms.Form):
    nombremanager = forms.CharField(max_length=30)
    fechanacmanager = forms.DateField()

    def clean(self):
        cleaned_data = super(managerForm, self).clean()
        nombremanager = cleaned_data.get('nombremanager')
        fechanacmanager = cleaned_data.get('fechanacmanager')
        if not nombremanager and not fechanacmanager:
            raise forms.ValidationError('Escribe algo!')

class discoForm(forms.Form):
    nombredisco = forms.CharField(max_length=30)
    nocanciones = forms.IntegerField()
    artista = forms.CharField(max_length=30)
    ano = forms.DateField()

    def clean(self):
        cleaned_data = super(discoForm, self).clean()
        nombredisco = cleaned_data.get('nombredisco')
        nocanciones = cleaned_data.get('nocanciones')
        artista = cleaned_data.get('artista')
        ano = cleaned_data.get('ano')
        if not nombredisco and not artista:
            raise forms.ValidationError('Escribe algo!')

class cancionForm(forms.Form):
    nombrecancion = forms.CharField(max_length=30)
    anodisco = forms.DateField()

    def clean(self):
        cleaned_data = super(cancionForm, self).clean()
        nombrecancion = cleaned_data.get('nombrecancion')
        anodisco = cleaned_data.get('ano')
        if not nombrecancion and not anodisco:
            raise forms.ValidationError('Escribe algo!')

class musicoForm(forms.Form):
    nombremusico = forms.CharField(max_length=30)
    fechanacmusico = forms.DateField()
    nodiscosmusico = forms.IntegerField()

    def clean(self):
        cleaned_data = super(musicoForm, self).clean()
        nombremusico = cleaned_data.get('nombremusico')
        fechanacmusico = cleaned_data.get('fechanacmusico')
        nodiscosmusico = cleaned_data.get('fechanacmusico')

        if not nombremusico and not nodiscosmusico:
            raise forms.ValidationError('Escribe algo!')




