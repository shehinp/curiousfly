# Generated by Django 4.1.2 on 2022-10-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0021_remove_address_username_address_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.AddField(
            model_name='address',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
