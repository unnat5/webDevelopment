# Generated by Django 4.1 on 2023-05-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0002_airport_alter_flights_destination_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Passenger",
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
                ("firstName", models.CharField(max_length=64)),
                ("lastName", models.CharField(max_length=64)),
                (
                    "flight",
                    models.ManyToManyField(
                        blank=True, related_name="passengers", to="flights.flights"
                    ),
                ),
            ],
        ),
    ]
