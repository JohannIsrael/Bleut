from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Quienes_Somos/', views.quienes_somos, name='quienesSomos'),
    path('Soporte/', views.soporte, name='soporte'),
    path('Contacto/', views.contacto, name='contacto'),
    path('perfil/', views.perfil, name='perfil'),
]
