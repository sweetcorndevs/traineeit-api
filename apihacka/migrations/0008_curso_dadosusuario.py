# Generated by Django 3.1.2 on 2021-01-17 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apihacka', '0007_remove_curso_dadosusuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='dadosusuario',
            field=models.ManyToManyField(blank=True, related_name='aula', to='apihacka.Curso'),
        ),
    ]
