# Generated by Django 5.0 on 2024-05-26 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0007_alter_institucion_img_perfil'),
        ('profesor', '0009_remove_profesor_carrera_remove_profesor_institucion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='institucion',
            field=models.ManyToManyField(related_name='profesor_instituciones', to='institucion.institucion'),
        ),
    ]
