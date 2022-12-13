from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . models import SignupUser
from ..trabajadores.models import SolicitudTrabajador

class LoginForm(forms.Form):
    username = forms.CharField(      
        required=True,
        widget=forms.TextInput(
           attrs={               
                "placeholder":"",
                "class":"main__input",
                "autocomplete":"off"
            } 
        )
    )

    password = forms.CharField(        
        required=True,
        widget=forms.PasswordInput(
           attrs={              
                "placeholder":"",
                "class":"main__input",
                # "autocomplete":"off"
            } 
        )
    )

class SignUpForm(UserCreationForm):

    username = forms.CharField(
       
        required=True,
        widget=forms.TextInput(
           attrs={
                "placeholder":"",
                "class":"sigc-input"
            } 
        )
    )

    first_name = forms.CharField(
        # label='Username',
        
        required=True,
        widget=forms.TextInput(
           attrs={
                "placeholder":"",
                "class":"sigc-input"
            } 
        )
    )

    last_name = forms.CharField(
        # label='Username',
        
        required=True,
        widget=forms.TextInput(
           attrs={
                "placeholder":"",
                "class":"sigc-input"
            } 
        )
    )


    email = forms.EmailField(
        # label='Email',
        
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder":"",
                "class":"sigc-input",
                "maxlength":"256",
            } 
        )
    )

    password1 = forms.CharField(
        # label='Password1',
        
        required=True,
        widget=forms.PasswordInput(
           attrs={
                "placeholder":"",
                "class":"sigc-input"
            } 
        )
    )

    password2 = forms.CharField(
        # label='Password2',
        
        required=True,
        widget=forms.PasswordInput(
           attrs={
                "placeholder":"",
                "class":"sigc-input"
            } 
        )
    )

    class Meta:
        model= User
        fields = ('username','first_name','last_name','email','password1','password2')

class CustomerForm(forms.ModelForm):

    cel = forms.CharField(
        
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "sigc-input",
                "minlength":"10",
                "maxlength":"10",
            }
        )
    )

    num = forms.CharField(
        # label='Cel',
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "sigc-input",
                "maxlength":"10",
            }
        )
    )

    calle = forms.CharField(
        # label='Cel',
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "sigc-input",
            }
        )
    )

    ciudad = forms.CharField(
        # label='Cel',
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "sigc-input",
            }
        )
    )

    imagen=forms.CharField(
        required=False,
        label='',
        widget=forms.FileInput(
            attrs={
                "placeholder": "",
                "class": "form__file",
                "accept":"image/*",
                "style":"color: transparent",
            }
        )
    )
    
    class Meta:
        model = SignupUser
        fields = ('cel','imagen','ciudad', 'calle', 'num')

class Solicitud(forms.Form):

    curriculum = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "accept":".pdf",
                "class": "sigc-input",
                "name":"file"
            }
        )
    )

