# Generated by Django 4.1.2 on 2022-10-12 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0017_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='organisation',
        ),
    ]
