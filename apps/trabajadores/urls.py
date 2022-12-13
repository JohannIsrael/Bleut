from django.urls import path
from . import views

urlpatterns = [
    path('oficio/crear', views.Oficios, name='oficios')
]