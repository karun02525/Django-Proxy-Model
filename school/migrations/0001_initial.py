# Generated by Django 4.2 on 2023-05-04 06:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExamCenter",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("cname", models.CharField(max_length=20)),
                ("city", models.CharField(max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Teacher",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                ("city", models.CharField(max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "examcenter_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        to="school.examcenter",
                    ),
                ),
                (
                    "base_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("roll", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
            bases=("school.examcenter",),
        ),
    ]
