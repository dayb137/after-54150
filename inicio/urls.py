from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio)
]
