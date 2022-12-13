from django.shortcuts import render
from ..authentication.models import User, SignupUser
from ..authentication.forms import  SignUpForm, CustomerForm
# from ..authentication.decorators import val_authentication
from django.utils.decorators import method_decorator
from ..trabajadores.models import SignupTrabajador, Licencia, Oficio_trabajador
from django.contrib.auth.decorators import login_required
from django.db.models import Count
# Create your views here.
def home(request):
    oficios = Oficio_trabajador.objects.all()
    return render(request,'home/home.html',{"oficios":oficios, })

def quienes_somos(request):
      
    return render(request,'home/quienesSomos.html',{})

def soporte(request):  
    return render(request, 'home/soporte.html',{})

def contacto(request):
   
    return render(request, 'home/contacto.html',{})

@login_required(login_url='auth_login')
def perfil(request):



    msg=None
    tipo_user=None 
    tipo_user = SignupUser.objects.filter(id_user_django=request.user).values()
    username = User.objects.get(username=request.user )
  
    django_profile = User.objects.filter(username=username)
    perfil = SignupUser.objects.filter(id_user_django=username)
    trabajador = SignupTrabajador.objects.filter(id_user_trabajador=username).values() 

    # _id = SignupTrabajador.objects.annotate() 
    # idlice = _id[0].Estrabajador
    # datos_licencia = Licencia.objects.filter(id=3).values()  
    # print(trabajador)
    # print(idlice)
    # print(datos_licencia) 
      
    context = {       
        "msg": msg,
        "datos_user":perfil,
        "django_profile":django_profile,
        "datos_trabajador":trabajador,
        "tipo_user":tipo_user,
        # "datos_licencia":datos_licencia,
    }


    return render(request, 'home/perfil.html',context)

@login_required(login_url='auth_login')
def historiales(request):
    tipo_user = SignupUser.objects.filter(id_user_django=request.user)

    context = {               
        "tipo_user":tipo_user,
        "user":tipo_user,
    }


    return render(request, 'home/historial.html',context)
