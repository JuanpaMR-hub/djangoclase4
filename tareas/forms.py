from django import forms
from . import models

class TareasFormExtended(forms.ModelForm):
    class Meta:
        model = models.Tarea
        fields = ['titulo','descripcion','completado']

        widgets = {
            'titulo':forms.TextInput(attrs={'autocomplete':'off'})
        }

        labels = {
            'titulo':'',
            'descripcion':'',
            'completado':'',
        }