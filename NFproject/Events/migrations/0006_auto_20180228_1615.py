# Generated by Django 2.0.2 on 2018-02-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0005_auto_20180228_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='types',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]