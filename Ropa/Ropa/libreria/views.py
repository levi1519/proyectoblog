from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ropa
from .forms import RopaForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def ropas(request):
    ropas = Ropa.objects.all()
    return render(request, 'ropas/index.html', {'ropas': ropas})

def crear(request):
    formulario = RopaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('ropas')
    return render(request, 'ropas/crear.html', {'formulario': formulario})

def editar(request, id):
    ropas = Ropa.objects.get(id=id)
    formulario = RopaForm(request.POST or None, request.FILES or None, instance=ropas)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('ropas')
    return render(request, 'ropas/editar.html', {'formulario': formulario})
def eliminar(request, id):
    ropas = Ropa.objects.get(id=id)
    ropas.delete() 
    return redirect('ropas')   