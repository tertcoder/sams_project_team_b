# Generated by Django 5.1.2 on 2024-10-11 06:39

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Admin",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("username", models.CharField(max_length=30, unique=True)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Lecturer",
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
                ("first_name", models.CharField(default="Unknown", max_length=100)),
                ("last_name", models.CharField(default="Unknown", max_length=100)),
                ("birthdate", models.DateField(default=django.utils.timezone.now)),
                ("phone", models.CharField(blank=True, max_length=15, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("username", models.CharField(default="Unknown", max_length=50)),
                ("password", models.CharField(default="Unknown", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("first_name", models.CharField(default="Unknown", max_length=100)),
                ("last_name", models.CharField(default="Unknown", max_length=100)),
                ("birthdate", models.DateField(default=django.utils.timezone.now)),
                ("phone", models.CharField(blank=True, max_length=15, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("username", models.CharField(default="Unknown", max_length=50)),
                ("password", models.CharField(default="Unknown", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
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
                ("course_code", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=255)),
                ("hours", models.IntegerField()),
                (
                    "lecturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="attendance.lecturer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attendance",
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
                (
                    "status",
                    models.CharField(
                        choices=[("P", "Present"), ("A", "Absent"), ("L", "Late")],
                        max_length=1,
                    ),
                ),
                ("date", models.DateField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="attendance.course",
                    ),
                ),
                (
                    "lecturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="attendance.lecturer",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="attendance.student",
                    ),
                ),
            ],
        ),
    ]
