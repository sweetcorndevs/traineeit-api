# Generated by Django 3.1.2 on 2021-01-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apihacka', '0010_auto_20210117_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario_aula',
            name='presente',
            field=models.BooleanField(default=False),
        ),
    ]