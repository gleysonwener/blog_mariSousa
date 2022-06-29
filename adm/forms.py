from django import forms
from categorias.models import Categoria
from posts.models import Post
from .models import ImagenPrincipal


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nome_categoria',]

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class PostPrincipalForm(forms.ModelForm):
    class Meta:
        model = ImagenPrincipal
        fields = '__all__'


