from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.forms import *
from .models import Perfil


def registro(request):

    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(user=user)
            return redirect("login")
    else:
        form = RegistroUsuarioForm()
        
    return render(request, "accounts/registro.html", {"form": form})


@login_required
def perfil(request):
    perfil_usuario, creado = Perfil.objects.get_or_create(user=request.user) # (Perfil, True) Si creo el perfil / (Perfil, False) si encontre el perfil y no lo creo.
    return render(request, "accounts/perfil.html", {"perfil": perfil_usuario})


@login_required
def editar_perfil(request):
    perfil_usuario, creado = Perfil.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil_usuario)
        
        if form.is_valid():
            form.save()
            return redirect("perfil")
    else:
        form = PerfilForm(instance=request.user)
        
    return render(request, "accounts/editar_perfil.html", {"form": form})
