# Generated by Django 3.1.2 on 2021-01-16 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255)),
                ('datahora', models.DateField(blank=True, max_length=200)),
                ('linkmeet', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255)),
                ('descricao', models.CharField(blank=True, max_length=255)),
                ('datahora', models.DateField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('googleid', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apihacka.curso')),
                ('id_usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='apihacka.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presente', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=255)),
                ('nota', models.IntegerField(blank=True, max_length=2)),
                ('linkaluno', models.CharField(blank=True, max_length=500)),
                ('id_aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apihacka.aula')),
                ('id_usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='apihacka.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='aula',
            name='id_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apihacka.curso'),
        ),
    ]