# Generated by Django 2.0.2 on 2018-02-28 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_auto_20180227_1509'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'ordering': ['-date']},
        ),
    ]
