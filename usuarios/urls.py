from django.urls import path
from . import views



app_name = 'usuarios'

urlpatterns = [
    path('login/', views.usuario_login, name='usuario_login'),
    path('logout/', views.usuario_logout, name='usuario_logout'),
]