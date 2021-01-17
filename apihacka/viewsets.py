from rest_framework import viewsets
from . import models
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter



class UsuarioViewset(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class AulaViewset(viewsets.ModelViewSet):
    queryset = models.Aula.objects.all()
    serializer_class = serializers.AulaSerializer

class Usuario_AulaViewset(viewsets.ModelViewSet):
    queryset = models.Usuario_Aula.objects.all().order_by('aula')
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

class Usuario_AulaLeituraViewset(viewsets.ModelViewSet):
    queryset = models.Usuario_Aula.objects.all().order_by('aula')
    serializer_class = serializers.Usuario_AulaLeituraSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ["curso", "aula"]

class LoginViewset(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.LoginSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ["googleid"]
