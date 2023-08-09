# Generated by Django 4.2.4 on 2023-08-08 12:58

from django.db import migrations


def func(apps, schema_editor):
    from django.core.management import call_command

    call_command("loaddata", "fixture_data.json")


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(func, reverse_func),
    ]
