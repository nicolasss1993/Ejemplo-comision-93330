from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    return render(request, "blog/inicio.html")


def contacto(request):
    return HttpResponse("Página de contacto")
