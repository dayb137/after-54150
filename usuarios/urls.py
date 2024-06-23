from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios import views

urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='usuarios/cierre_de_sesion.html'), name='logout'),
    path('login/',views.login, name='login'),
    path('registro/',views.registro, name='registro'),
    
    
]
