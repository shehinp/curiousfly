# Generated by Django 4.1.2 on 2022-10-12 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0020_remove_address_user_address_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='username',
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='useraddress', to=settings.AUTH_USER_MODEL),
        ),
    ]
