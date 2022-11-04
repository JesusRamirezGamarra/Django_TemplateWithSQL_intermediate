# Generated by Django 4.1.1 on 2022-11-01 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0029_remove_usercolaborator_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postusercolaborator',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usercolaborator',
            name='perfil',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.perfil'),
        ),
        migrations.AlterField(
            model_name='usercolaborator',
            name='suscripcion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.suscripcion'),
        ),
    ]
