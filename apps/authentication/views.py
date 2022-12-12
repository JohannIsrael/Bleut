from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, SignUpForm, CustomerForm, Solicitud
from ..trabajadores.models import SolicitudTrabajador
from ..clientes.models import SignupCliente


# Create your views here.
def view_login(request):
    
    msg = None
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg = "usuario o contraseña incorrecta"
        else:
            print('no es valido')

    return render(request,'authentication/login.html',{"form":form, "msg":msg})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)   
    return redirect('home')

def sigup_cliente(request):

    signup_form = SignUpForm(request.POST or None, prefix='signup')
    customer_form = CustomerForm(request.POST or None, prefix='customer')
    
    msg = None

    if request.method == "POST":

        if signup_form.is_valid() and customer_form.is_valid():
            
            user_form = signup_form.save()
            new_customer = customer_form.save(commit=False)
            
            username = signup_form.cleaned_data.get('username')
            password = signup_form.cleaned_data.get('password1')
            

            user = authenticate(username=username, password=password)
            if user is not None:
                
                new_customer.user = user
                new_customer.save()

                cliente = SignupCliente.objects.create(id_user=user)
                cliente.save()

                login(request, user)
                return redirect('home')
            else:
                msg = "Erro al autentificar"

        else:
            msg = 'Error al registrar usuario: '
    
    context = {
        "signup_form": signup_form,
        "customer_form": customer_form,
        "msg": msg,
    }

    return render(request, 'authentication/signup_customer.html',context)

def solicitud_trabajadores(request):

    
    signup_form = SignUpForm(request.POST or None, prefix='signup')
    customer_form = CustomerForm(request.POST or None, prefix='customer')
    msg = None
    form = Solicitud()

    if request.method == "POST":

        form = Solicitud(request.POST or None, request.FILES or None)     
         

        if  form.is_valid() and signup_form.is_valid() and customer_form.is_valid():         
            _file = form.cleaned_data.get("curriculum")          

            solicitud = SolicitudTrabajador.objects.create(curriculum=_file)         
            user_form = signup_form.save()
            new_customer = customer_form.save(commit=False)
            
            username = signup_form.cleaned_data.get('username')
            password = signup_form.cleaned_data.get('password1')           
            user = authenticate(username=username, password=password)         
            msg = "Formulario enviado, espere la respuesta en su correo"  
            if user is not None:                
                new_customer.user = user
                new_customer.save()
                solicitud.save()                    
        else:
            msg = "Error al registrase"

    context = {
        "form": form,
        "signup_form": signup_form,
        "customer_form": customer_form,
        "msg": msg,
    }
    
    
    return render(request,'authentication/signup_worker.html',context) 

