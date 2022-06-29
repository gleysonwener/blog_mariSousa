from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from adm.forms import CategoriaForm, PostForm
from posts.models import Post
from categorias.models import Categoria
from posts.models import Post
from comentarios.models import Comentario
from comentarios.forms import FormComentario
from .forms import PostPrincipalForm
from .models import ImagenPrincipal
from django.db.models import Q

@login_required
def principal(request):
    template_name = 'adm/principal.html'

    cont_posts = Post.objects.filter()
    cont_comentarios = Comentario.objects.filter()

    ultimos_posts = Post.objects.all().order_by('-id')[:4]
    ultimos_comentarios = Comentario.objects.all().order_by('-id')[:4]

    context = {
        'ultimos_posts': ultimos_posts,
        'ultimos_comentarios': ultimos_comentarios,
        'cont_posts': cont_posts,
        'cont_comentarios': cont_comentarios,
    }
    return render(request, template_name, context)

@login_required
def nova_categoria(request):
    template_name = 'adm/nova_categoria.html'
    context = {}
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            cat_form = form.save(commit=False)
            cat_form.usuario = request.user
            cat_form.save()
            messages.success(request, 'Categoria adicionada com sucesso')
            return redirect('adm:lista_categoria')
    else:
        form = CategoriaForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required
def lista_categoria(request):
    template_name = 'adm/lista_categoria.html'
    categorias = Categoria.objects.all().order_by('-id')[:8]
    context ={
        'categorias': categorias
    }

    return render(request, template_name,context)

@login_required
def editar_categoria(request, pk):
    template_name = 'adm/nova_categoria.html'
    context = {}

    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist as e:
        messages.warning(request, 'Você não tem permissão para editar a categoria informada.')
        return redirect('adm:lista_categoria')

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso.')
            return redirect('adm:lista_categoria')
    else:
        form = CategoriaForm(instance=categoria)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def deletar_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
        categoria.delete()
    except Categoria.DoesNotExist as e:
        messages.warning('request', 'Você não tem permissão para apagar a categoria.')
        return redirect('adm:lista_categoria')
    messages.info(request, 'Categoria Apagada')
    return redirect('adm:lista_categoria')


@login_required
def lista_post(request):
    template_name = 'adm/lista_post.html'
    posts = Post.objects.all().order_by('-id')[:8]
    context = {
        'posts': posts
    }
    return render(request, template_name, context)


@login_required
def novo_post(request):
    template_name = 'adm/novo_post.html'
    context = {}

    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.usuario = request.user
            post_form.save()
            messages.success(request, 'Post adcionado com sucesso.')
            return redirect('adm:lista_post')
    else:
        form = PostForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def editar_post(request, pk):
    template_name = 'adm/novo_post.html'
    context = {}
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post atualizado com sucesso.')
            return redirect('adm:lista_post')
    else:
        form = PostForm(instance=post)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def deletar_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        post.delete()
    except Post.DoesNotExist as e:
        messages.warning('request', 'Você não tem permissão para apagar o post.')
        return redirect('adm:lista_post')
    messages.info(request, 'Post apagado com suceso.')
    return redirect('adm:lista_post')


@login_required
def lista_comentario(request):
    template_name = 'adm/lista_comentario.html'
    comentarios = Comentario.objects.all().order_by('-id')
    context = {
        'comentarios': comentarios
    }
    return render(request, template_name, context)


@login_required
def novo_comentario(request):
    template_name = 'adm/novo_comentario.html'
    context = {}
    if request.method == 'POST':
        form = FormComentario(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comentário adicionado com sucesso.')
            return redirect('adm:lista_comentario')
    else:
        form = FormComentario()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def editar_comentario(request, pk,):
    template_name = 'adm/novo_comentario.html'
    context = {}
    comentarios = Comentario.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormComentario(request.POST or None, request.FILES or None, instance=comentarios)
        if form.is_valid():
            form_com = form.save(commit=False)
            form_com.publicado_comentario = True  # Muda o estatus para vizualizar o comentário
            form.save()
            messages.success(request, 'Comentário liberado com sucesso.')
            return redirect('adm:lista_comentario')
    else:
        form = FormComentario(instance=comentarios)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def deletar_comentario(request, pk):

    comentarios = Comentario.objects.get(pk=pk)
    comentarios.delete()
    messages.info(request, 'Comentário apagado com sucesso.')
    return redirect('adm:lista_comentario')


@login_required
def buscar(request):
    template_name = 'adm/busca_resultados.html'
    context = {}
    termo = request.GET.get('termo', None)

    if termo is not None:
        posts = Post.objects.busca(termo=termo)
        comentarios = Comentario.objects.busca(termo=termo)

        context['posts'] = posts
        context['comentarios'] = comentarios

    return render(request, template_name, context)



