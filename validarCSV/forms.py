from django import forms

class CargarArchivoCSV(forms.Form):
    file = forms.FileField(label="Selecciona el archivo CSV")
