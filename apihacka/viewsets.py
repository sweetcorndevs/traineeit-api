from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters


class UsuarioViewset(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class AulaViewset(viewsets.ModelViewSet):
    queryset = models.Aula.objects.all()
    serializer_class = serializers.AulaSerializer

class Usuario_AulaViewset(viewsets.ModelViewSet):
    queryset = models.Usuario_Aula.objects.all()
    serializer_class = serializers.Usuario_AulaSerializer

class CursoViewset(viewsets.ModelViewSet):
    queryset = models.Curso.objects.all()
    serializer_class = serializers.CursoSerializer


class UsuarioLeituraViewset(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioLeituraSerializer

class CursoLeituraViewset(viewsets.ModelViewSet):
    queryset = models.Curso.objects.all()
    serializer_class = serializers.CursoLeituraSerializer