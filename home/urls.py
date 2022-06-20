from django.urls import path
from .views import principal

app_name = 'home'

urlpatterns = [
    path('', principal, name='princial')
]