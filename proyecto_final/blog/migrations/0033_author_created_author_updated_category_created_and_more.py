# Generated by Django 4.1.1 on 2022-11-07 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_alter_author_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='author',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición'),
        ),
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición'),
        ),
        migrations.AddField(
            model_name='collaboration',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='collaboration',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición'),
        ),
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='contact',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición'),
        ),
        migrations.AddField(
            model_name='donation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='donation',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición'),
        ),
        migrations.AddField(
            model_name='donation_goal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='donation_goal',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición'),
        ),
        migrations.AddField(
            model_name='embrace',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='embrace',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición'),
        ),
        migrations.AddField(
            model_name='job',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='job',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición'),
        ),
        migrations.AddField(
            model_name='jobgroup',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='jobgroup',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición'),
        ),
        migrations.AddField(
            model_name='suscripcion',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='suscripcion',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición'),
        ),
    ]
