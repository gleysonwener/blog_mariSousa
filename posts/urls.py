from django.urls import path
from . import views
from adm import urls
from adm.views import contato


urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.PostCategoria.as_view(), name='post_categorias'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('post/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),
    path('contato/', contato, name='contato'),

]