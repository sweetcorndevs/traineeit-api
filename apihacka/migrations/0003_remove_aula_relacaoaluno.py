# Generated by Django 3.1.2 on 2021-01-17 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apihacka', '0002_curso_dadosusuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='relacaoaluno',
        ),
    ]