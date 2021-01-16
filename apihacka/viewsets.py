from rest_framework import viewsets
from . import models
from . import serializers

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class CursoViewset(viewsets.ModelViewSet):
    queryset = models.Curso.objects.all()
    serializer_class = serializers.CursoSerializer

class Usuario_CursoViewset(viewsets.ModelViewSet):
    queryset = models.Usuario_Curso.objects.all()
    serializer_class = serializers.Usuario_CursoSerializer

class AulaViewset(viewsets.ModelViewSet):
    queryset = models.Aula.objects.all()
    serializer_class = serializers.AulaSerializer

class Usuario_AulaViewset(viewsets.ModelViewSet):
    queryset = models.Usuario_Aula.objects.all()
    serializer_class = serializers.Usuario_AulaSerializer