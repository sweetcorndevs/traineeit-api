from rest_framework import serializers
from .models import Usuario, Curso, Aula, Usuario_Aula

        
class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = ('id', 'nome', 'datahora', 'linkmeet', 'curso')

class Usuario_AulaLeituraSerializer(serializers.ModelSerializer):
    curso = serializers.StringRelatedField()
    aula = serializers.StringRelatedField()
    aluno = serializers.StringRelatedField()
    class Meta:
        model = Usuario_Aula
        fields = ('curso', 'aula', 'aluno',  'presente', 'nota', 'linkaluno')


class Usuario_AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_Aula
        fields = ('curso', 'aula', 'aluno',  'presente', 'nota', 'linkaluno')
        


class CursoLeituraSerializer(serializers.ModelSerializer):
    aulas = AulaSerializer(many=True, read_only=False)
    class Meta:
        model = Curso
        fields = ('id', 'nome', 'descricao', 'totaldehoras', 'datahora', 'aulas')

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'nome', 'descricao', 'totaldehoras', 'datahora', 'aulas')

class UsuarioLeituraSerializer(serializers.ModelSerializer):
    cursos = CursoSerializer(many=True, read_only=False)
    class Meta:
        model = Usuario
        fields = ('id', 'tipousuario', 'nome', 'email', 'googleid', 'cursos')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'tipousuario', 'nome', 'email', 'googleid', 'cursos')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'tipousuario', 'email')


        

