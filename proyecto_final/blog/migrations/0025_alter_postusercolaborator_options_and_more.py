# Generated by Django 4.1.1 on 2022-10-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_perfil_suscripcion_usercolaborator_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postusercolaborator',
            options={'verbose_name_plural': 'User Post colaborators'},
        ),
        migrations.AlterField(
            model_name='usercolaborator',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='avatar'),
        ),
    ]
