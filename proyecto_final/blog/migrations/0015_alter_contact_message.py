# Generated by Django 4.1.2 on 2022-10-28 11:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0014_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact", name="message", field=ckeditor.fields.RichTextField(),
        ),
    ]