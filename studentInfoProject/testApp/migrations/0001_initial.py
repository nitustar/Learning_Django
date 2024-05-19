# Generated by Django 5.0.6 on 2024-05-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
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
                ("name", models.CharField(max_length=30)),
                ("rollno", models.IntegerField()),
                ("dob", models.DateField()),
                ("marks", models.IntegerField()),
                ("address", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("phonenumber", models.IntegerField(verbose_name=15)),
            ],
        ),
    ]
