# Generated by Django 4.1.2 on 2022-10-13 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0026_lead_facebook_ad_lead_fb_ad_campaign_lead_fb_ad_set_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='sec_email',
            new_name='secondary_email',
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='sec_phone',
            new_name='secondary_phone',
        ),
    ]
