from django.shortcuts import render,redirect
from Autosapp.models import Autos,Repuesto,Tienda
from . import forms
from Autosapp.forms import Registroform, RegistroR, RegistroT

# Create your views here.

def renderTemplate(request):
    autos = Autos.objects.all()
    data = {'Autos':autos}
    return render(request, 'Autosapp/Autosapp.html',data)

def renderTemplateR(request):
    repuesto = Repuesto.objects.all()
    data = {'Repuesto': repuesto}
    return render(request, 'Autosapp/CamposRe.html', data)


def renderTemplateT(request):
    tienda = Tienda.objects.all()
    data = {'Tienda': tienda}
    return render(request, 'Autosapp/CamposTi.html',data)

def RegistroRe(request):
    form = RegistroR()

    if request.method == 'POST':
        form = RegistroR(request.POST)
        if form.is_valid():
            form.save()
        return renderTemplateR(request)
    data = {'form': form}
    return render(request,'Autosapp/Repuesto.html',data)

def RegistroTi(request):
    form = RegistroT()

    if request.method == 'POST':
        form = RegistroT(request.POST)
        if form.is_valid():
            form.save()
        return renderTemplateT(request)
    data = {'form': form}
    return render(request,'Autosapp/Tienda.html',data)


    


def RegistroView(request):
    form = Registroform()

    if request.method == 'POST':
        form = Registroform(request.POST)
        if form.is_valid():
            form.save()
        return renderTemplate(request)   
    data = {'form':form}
    return render(request,'Autosapp/Registro.html',data)

def eliminarAutos(request, id):
    autos = Autos.objects.get(id = id)
    autos.delete()
    return redirect('/Autos')

def eliminarRepuesto(request, id):
    repuesto = Repuesto.objects.get(id = id)
    repuesto.delete()
    return redirect('/Repuesto')

def eliminarTienda(request, id):
    tienda = Tienda.objects.get(id = id)
    tienda.delete()
    return redirect('/Tienda')


def actualizarAutos(request,id):
    autos = Autos.objects.get(id = id)
    form = Registroform(instance=autos)
    if request.method == 'POST':
        form = Registroform(request.POST, instance=autos)
        if form.is_valid():
            form.save()
        return renderTemplate(request)
    data = {'form':form}
    return render(request,'Autosapp/Registro.html',data)    

def actualizarRepuesto(request,id):
    repuesto = Repuesto.objects.get(id = id)
    form = RegistroR(instance=repuesto)
    if request.method == 'POST':
        form = RegistroR(request.POST, instance=repuesto)
        if form.is_valid():
            form.save()
        return renderTemplateR(request)
    data = {'form':form}
    return render(request,'Autosapp/Repuesto.html',data)  

def actualizarTienda(request,id):
    tienda = Tienda.objects.get(id = id)
    form = RegistroT(instance=tienda)
    if request.method == 'POST':
        form = RegistroT(request.POST, instance=tienda)
        if form.is_valid():
            form.save()
        return renderTemplateT(request)
    data = {'form':form}
    return render(request,'Autosapp/Tienda.html',data)  