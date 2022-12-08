from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    foto = forms.CharField(max_length=100)

    class Meta:
        """ Vamos a indicar que este formualario pertenece a un modelo """
        model = User
        """ Podemos definir que campos seran los que mistremos usando el atributo fields """
        fields = ("username", "first_name", "last_name", "email",  "password1", "password2", "foto")

    """ Vamos a sobreescribir el metodo save """
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        # aumentar el email y foto
        user.email = self.cleaned_data['email']
        user.foto = self.cleaned_data['foto']
        if commit:
            user.save()
        return user