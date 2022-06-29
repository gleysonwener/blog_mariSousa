from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static



app_name = 'adm'

urlpatterns = [
    path('principal/', principal, name='principal'),
    path('lista_comentario/', lista_comentario, name='lista_comentario'),
    path('novo_comentario/', novo_comentario, name='novo_comentario'),
    path('editar_comentario/<int:pk>/', editar_comentario, name='editar_comentario'),
    path('deletar_comentario/<int:pk>/', deletar_comentario, name='deletar_comentario'),
    path('nova_categoria/', nova_categoria, name='nova_categoria'),
    path('lista_categoria/', lista_categoria, name='lista_categoria'),
    path('editar_categoria/<int:pk>/', editar_categoria, name='editar_categoria'),
    path('deletar_categoria/<int:pk>/', deletar_categoria, name='deletar_categoria'),
    path('lista_post/', lista_post, name='lista_post'),
    path('novo_post/', novo_post, name='novo_post'),
    path('editar_post/<int:pk>/', editar_post, name='editar_post'),
    path('deletar_post/<int:pk>/', deletar_post, name='deletar_post'),
    path('buscar/', buscar, name='buscar'),
    path('novo_post_principal/', novo_post_principal, name='novo_post_principal'),
    path('lista_novo_post_principal/', lista_novo_post_principal, name='lista_novo_post_principal'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)