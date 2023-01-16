from django import forms 

class FormularioContacto(forms.Form):
    nombre= forms.CharField(label="Nombre", required=True ,max_length=30)
    Email = forms.EmailField(label="Email", required=True ,max_length=30)
    Contenido= forms.CharField(label="Contenido", widget=forms.Textarea)
