# Generated by Django 4.2.1 on 2023-05-16 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("weather", "0003_alter_city_options"),
    ]

    operations = [
        migrations.AlterModelOptions(name="city", options={"ordering": ("-created",)},),
    ]