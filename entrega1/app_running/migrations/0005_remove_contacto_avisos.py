# Generated by Django 4.0.4 on 2022-07-04 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_running', '0004_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='avisos',
        ),
    ]