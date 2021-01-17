from django.db import models
from datetime import datetime

# Create your models here.



tipo = [
    ('Aluno', 'Aluno'),
    ('Empresa', 'Empresa'),
    ('Professor', 'Professor'),
]



class Aula(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(max_length=255, blank=True)
    datahora = models.DateTimeField(blank=True)
    linkmeet = models.CharField(max_length=500, blank=True)
    curso = models.ForeignKey("Curso", blank=True, on_delete=models.CASCADE, related_name='+')
    relacaoaluno = models.ForeignKey("Usuario_Aula", blank=True, on_delete=models.CASCADE, related_name='+')
    

    def __str__(self):
        return self.nome


class Usuario_Aula(models.Model):
    presente = models.BooleanField(default=False)
    nota = models.IntegerField(max_length=2, blank=True)
    linkaluno = models.CharField(max_length=500, blank=True)
    aluno = models.ForeignKey("Usuario", blank=True, on_delete=models.CASCADE, related_name='+')
    aula = models.ForeignKey("Aula", blank=True, on_delete=models.CASCADE, related_name='+')
    curso = models.ForeignKey("Curso", blank=True, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.aluno

class Curso(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(max_length=255, blank=True)
    datahora = models.DateTimeField(blank=True)
    totaldehoras = models.IntegerField(max_length=4, blank=True)
    aulas = models.ManyToManyField(Aula, blank=True, related_name='aula')


    def __str__(self):
        return self.nome

    def natural_key(self):
        return self.aulas

class Usuario(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    googleid = models.CharField(max_length=5000, blank=True)
    tipousuario = models.CharField(max_length=255, choices=tipo, blank=True)
    cursos = models.ManyToManyField('Curso', blank=True, related_name='+')
    

    def __str__(self):
        return self.nome


