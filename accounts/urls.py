from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('actualizar/', views.actualizar_perfil, name='actualizar_perfil'),
    path('iniciar_sesion/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('cerrar_sesion/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout')
]