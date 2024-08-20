from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User,Group
from .models import Arrendatario, Propietario



class ModificarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario", max_length=100)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)



class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    TIPO_USUARIO_CHOICES = [
        ('propietario', 'Propietario'),
        ('arrendatario', 'Arrendatario'),
    ]
    
    tipo_usuario = forms.ChoiceField(choices=TIPO_USUARIO_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'tipo_usuario']

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


    

class ArrendatarioForm(forms.ModelForm):
    class Meta:
        model = Arrendatario
        fields = ['nombre', 'correo']

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'correo']
