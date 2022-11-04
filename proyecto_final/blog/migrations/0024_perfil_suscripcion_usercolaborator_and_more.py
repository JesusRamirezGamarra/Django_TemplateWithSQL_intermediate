# Generated by Django 4.1.1 on 2022-10-29 13:05

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_delete_postusercolaborator_delete_usercolaborator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'User Colaborator Perfils',
            },
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'User Colaborator Suscripcions',
            },
        ),
        migrations.CreateModel(
            name='UserColaborator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('username', models.CharField(max_length=70)),
                ('pwd', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('profile_picture', models.ImageField(blank=True, upload_to='')),
                ('createdate', models.DateTimeField(auto_now_add=True, null=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.perfil')),
                ('suscripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.suscripcion')),
            ],
            options={
                'verbose_name_plural': 'User colaborators',
            },
        ),
        migrations.CreateModel(
            name='PostUserColaborator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('createdate', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.usercolaborator')),
            ],
            options={
                'verbose_name_plural': 'Post user colaborators',
            },
        ),
    ]