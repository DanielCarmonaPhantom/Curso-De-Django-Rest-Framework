from email import message
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework import viewsets


from profiles_api import serializers



# Create your views here.

class HelloAPIView(APIView):


    """ API view de Prueba """

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """ Retornar lista de caracteristicas del APIView"""

        an_apiview = [
            'Usamos metodos HTTP como funciones(get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la lógica de nuestra aplicación',
            'Esta mapeado manualmente a los URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Crea un mensaje con nuestro nombre """
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializers.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """ Maneja actualizar un objeto """
        return Response({'method': 'PUT'})

    def path(self, request, pk=None):
        """ Maneja actualizacion parcial de un objeto """
        return Response({'method': 'Patch'})

    def delete(self, request, pk=None):
        """ Borra un objeto """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ TEST Api ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """" Retornar un Mensaje de Hola Mundo"""

        a_viewset = [
            'Usa acciones list, create, retrieve, update, partial_update',
            'Automaticamente mapea a los URLs usando RRouters',
            'Probe más funcionalidad con menos código'
        ]
        return Response({'message': 'Hola', 'a_viewset': a_viewset})

    def create(self, request):
        """ Crear nuevo mensaje de hola mundo """
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hola {name}'
            return Response({'message': message})
        else:
            return Response(
                serializers.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Obtiene un Objeto y su ID """
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        """ Actualiza un Objeto """
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """ Actualiza parcialmente un Objeto """
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """ Destruye un Objeto """
        return Response({'http_method':'DELETE'})