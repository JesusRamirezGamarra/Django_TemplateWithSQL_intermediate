# Generated by Django 4.1.2 on 2022-10-28 12:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0016_alter_contact_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="embrace",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
