# Generated by Django 4.1.1 on 2022-11-01 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_alter_usercolaborator_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercolaborator',
            name='name',
        ),
        migrations.RemoveField(
            model_name='usercolaborator',
            name='pwd',
        ),
        migrations.RemoveField(
            model_name='usercolaborator',
            name='username',
        ),
    ]
