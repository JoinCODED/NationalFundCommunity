# Generated by Django 2.0.2 on 2018-03-05 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IndividualProfile',
            new_name='Individual',
        ),
        migrations.RenameModel(
            old_name='OrginizationProfile',
            new_name='Orginization',
        ),
    ]
