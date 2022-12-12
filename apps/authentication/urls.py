from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.view_login, name='auth_login'),
    path('signup_cliente/', views.sigup_cliente, name='signup_cliente'),
    path('signup_trabajador/', views.solicitud_trabajadores , name='signup_trabajador'),
    path('logout/', views.logout_view, name="auth_logout"),
]
