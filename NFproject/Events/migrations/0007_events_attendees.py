# Generated by Django 2.0.2 on 2018-03-06 12:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Events', '0006_auto_20180228_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='attendees',
            field=models.ManyToManyField(related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]