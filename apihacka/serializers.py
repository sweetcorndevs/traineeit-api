from rest_framework import serializers
from .models import Usuario, Curso, Usuario_Curso, Aula, Usuario_Aula

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'email', 'googleid')

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'nome', 'descricao', 'datahora')

class Usuario_CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_Curso
        fields = ('id_usuario', 'id_curso')

class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = ('nome', 'datahora', 'linkmeet', 'id_curso')

class Usuario_AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_Aula
        fields = ('presente', 'nota', 'linkaluno', 'id_aula', 'id_usuario')