# Generated by Django 4.0.4 on 2022-07-04 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_running', '0003_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]
