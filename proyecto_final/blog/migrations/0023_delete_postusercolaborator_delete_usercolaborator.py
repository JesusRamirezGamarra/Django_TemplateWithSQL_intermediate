# Generated by Django 4.1.1 on 2022-10-29 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_postusercolaborator_createdate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostUserColaborator',
        ),
        migrations.DeleteModel(
            name='UserColaborator',
        ),
    ]
