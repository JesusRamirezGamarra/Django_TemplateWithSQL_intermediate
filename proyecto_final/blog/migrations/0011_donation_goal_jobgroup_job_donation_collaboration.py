# Generated by Django 4.1.2 on 2022-10-09 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_remove_donation_donation_goal_remove_donation_jobrol_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Donation_Goal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("goal", models.IntegerField()),
                ("description", models.CharField(max_length=500)),
                ("startdate", models.DateField()),
                ("enddate", models.DateField()),
                ("active", models.BooleanField()),
                ("createdate", models.DateTimeField(auto_now_add=True)),
            ],
            options={"verbose_name_plural": "Donations Goal",},
        ),
        migrations.CreateModel(
            name="JobGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("createdate", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("createdate", models.DateTimeField(auto_now_add=True)),
                (
                    "jobgroup",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.jobgroup"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Donation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firtsname", models.CharField(max_length=50)),
                ("lastname", models.CharField(max_length=50)),
                ("telephone", models.CharField(max_length=15)),
                ("company", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("dateofbirht", models.DateField()),
                ("createdate", models.DateTimeField(auto_now_add=True)),
                (
                    "donation_Goal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.donation_goal",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.job"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Collaboration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.IntegerField()),
                ("createdate", models.DateTimeField(auto_now_add=True)),
                (
                    "donation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.donation"
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.job"
                    ),
                ),
            ],
        ),
    ]