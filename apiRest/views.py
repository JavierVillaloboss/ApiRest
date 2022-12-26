from django.shortcuts import render
from .serializers import autosSerializer,tiendaSerializer,repuestoSerializer
from .models import Autos,Tienda,Repuesto
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#Autos
@api_view(['GET','POST'])
def autos_list(request):
    if request.method == 'GET':
        autos = Autos.objects.all()
        serializer = autosSerializer(autos, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = autosSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def autos_detail(request,pk):
    try:
        autos = Autos.objects.get(pk = pk)
    except Autos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = autosSerializer(autos)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = autosSerializer(autos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        autos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Tienda

@api_view(['GET','POST'])
def tienda_list(request):
    if request.method == 'GET':
        tienda = Tienda.objects.all()
        serializer = tiendaSerializer(tienda, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = tiendaSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
@api_view(['GET','PUT','DELETE'])
def tienda_detail(request,pk):
    try:
        tienda = Tienda.objects.get(pk = pk)
    except Tienda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = tiendaSerializer(tienda)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = tiendaSerializer(tienda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        tienda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Repuesto
@api_view(['GET','POST'])
def repuesto_list(request):
    if request.method == 'GET':
        repuesto = Repuesto.objects.all()
        serializer = repuestoSerializer(repuesto, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = repuestoSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
@api_view(['GET','PUT','DELETE'])
def repuesto_detail(request,pk):
    try:
        repuesto = Repuesto.objects.get(pk = pk)
    except Repuesto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = repuestoSerializer(repuesto)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = repuestoSerializer(repuesto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        repuesto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

