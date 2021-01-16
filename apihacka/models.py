from django.db import models

# Create your models here.

choice = [
    ('Sim', 'Sim'),
    ('Não', 'Não'),
]

class Usuario(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    googleid = models.CharField(max_length=500, blank=True)

class Curso(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(max_length=255, blank=True)
    datahora = models.DateField(max_length=200, blank=True)

class Usuario_Curso(models.Model):
    id_usuario = models.ForeignKey(Usuario, default=None, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)


class Aula(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    datahora = models.DateField(max_length=200, blank=True)
    linkmeet = models.CharField(max_length=500, blank=True)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Usuario_Aula(models.Model):
    presente = models.CharField(max_length=255, choices=choice, blank=True)
    nota = models.IntegerField(max_length=2, blank=True)
    linkaluno = models.CharField(max_length=500, blank=True)
    id_aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, default=None, on_delete=models.CASCADE)