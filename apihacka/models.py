from django.db import models
from datetime import datetime

# Create your models here.

choice = [
    ('Sim', 'Sim'),
    ('Não', 'Não'),
]

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
    curso = models.ForeignKey("Curso", blank=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nome


class Usuario_Aula(models.Model):
    presente = models.CharField(max_length=255, choices=choice, blank=True)
    nota = models.IntegerField(max_length=2, blank=True)
    linkaluno = models.CharField(max_length=500, blank=True)
    aluno = models.ForeignKey("Usuario", blank=True, on_delete=models.CASCADE)
    aula = models.ForeignKey("Aula", blank=True, on_delete=models.CASCADE)
    curso = models.ForeignKey("Curso", blank=True, on_delete=models.CASCADE)

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
    googleid = models.CharField(max_length=500, blank=True)
    tipousuario = models.CharField(max_length=255, choices=tipo, blank=True)
    cursos = models.ManyToManyField('Curso', blank=True)
    

    def __str__(self):
        return self.nome


