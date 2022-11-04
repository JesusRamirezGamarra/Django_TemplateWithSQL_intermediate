# Generated by Django 4.1.1 on 2022-10-28 21:56

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_embrace_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserColaborator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70)),
                ('pwd', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='embrace',
            name='description',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='PostUserColaborator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.usercolaborator')),
            ],
        ),
    ]