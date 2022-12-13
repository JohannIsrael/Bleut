from django.shortcuts import render, redirect
from ..authentication.models import User, SignupUser
from ..authentication.forms import  SignUpForm, CustomerForm
from ..trabajadores.models import SignupTrabajador, Licencia
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='auth_login')
def Oficios(request):

    return render(request, 'worker/oficios.html', {})




