from rest_framework import viewsets
from . import models
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend



class UsuarioViewset(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class AulaViewset(viewsets.ModelViewSet):
    queryset = models.Aula.objects.all()
    serializer_class = serializers.AulaSerializer

class Usuario_AulaViewset(viewsets.ModelViewSet):
    queryset = models.Usuario_Aula.objects.all()
    serializer_class = serializers.Usuario_AulaSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ["curso"]


class CursoViewset(viewsets.ModelViewSet):
    queryset = models.Curso.objects.all()
    serializer_class = serializers.CursoSerializer


class UsuarioLeituraViewset(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioLeituraSerializer

class CursoLeituraViewset(viewsets.ModelViewSet):
    queryset = models.Curso.objects.all()
    serializer_class = serializers.CursoLeituraSerializer