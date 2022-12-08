from django import forms

class PortafolioForm(forms.Form):
  titulo = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
    "class": "form-control mb-3"
  }))
  descripcion = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
    "class": "form-control mb-3"
  }))
  tag = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
    "class": "form-control mb-3"
  }))
  url = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
    "class": "form-control mb-3"
  }))