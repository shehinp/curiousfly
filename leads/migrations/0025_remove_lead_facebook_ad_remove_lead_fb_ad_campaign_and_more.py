# Generated by Django 4.1.2 on 2022-10-12 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0024_alter_lead_phone_number_alter_lead_sec_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='facebook_ad',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='fb_ad_campaign',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='fb_ad_set',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='fb_page',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='google_campaign',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='no_of_employees',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='sec_email',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='sec_phone',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='website',
        ),
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]