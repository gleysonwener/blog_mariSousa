from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from usuarios.forms import UsuarioLogin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from adm import urls



def usuario_login(request):
    template_name = 'usuarios/login.html'
    context = {}

    if request.method == 'POST':
        form = UsuarioLogin(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']
            user = authenticate(username=usuario, password=senha)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login com sucesso.')
                return redirect('adm:principal')
            else:
                messages.warning(request, 'Sua conta está inativa, contate o suporte.')
                return redirect('usuarios:usuario_login')
        else:
            messages.error(request, 'Usuários ou senha inválidos.')
            return redirect('usuarios:usuario_login')
    else:
        form = UsuarioLogin
        context['form'] = form

    return render(request, template_name, context)



def usuario_logout(request):
    logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('index')