# Generated by Django 5.0.4 on 2024-04-29 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0003_institucion_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='img_perfil',
            field=models.ImageField(blank=True, default='perfiles/IFTS/IFTS18-FRONT.jpg', null=True, upload_to='perfiles/IFTS/'),
        ),
    ]
