# Generated by Django 2.0.2 on 2018-03-12 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0009_auto_20180312_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='remaining_seats',
            new_name='seats_taken',
        ),
    ]