from django.shortcuts import render, redirect, get_object_or_404
from app import models, form

# Create your views here.

def inicio (i):
    return render(i,'inicio.html')

def lista (i):
    animales = models.animales.objects.all()
    return render(i,'lista.html',{
        'animales': animales
    })

def lista_d (i,id):
    animales = get_object_or_404(models.animales,id=id)
    atributos = models.atributos.objects.filter(animal_id=id)
    return render(i,'lista_d.html',{
        'atributos': atributos,
        'animales': animales
    })

def formulario (i):
    if i.method == 'GET':
        return render(i,'formulario.html',{
            'animales': form.animales,
            'atributos': form.atributos
        })
    else:
        if 'nombre' in i.POST:
            models.animales.objects.create(nombre=i.POST['nombre'])
        else:
            models.atributos.objects.create(
                animal_id=i.POST['animal'],
                descripcion=i.POST['descripcion']
            )
            return redirect ('formulario')
    
