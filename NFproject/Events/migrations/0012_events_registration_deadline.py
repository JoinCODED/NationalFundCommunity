# Generated by Django 2.0.2 on 2018-03-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0011_auto_20180312_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='registration_deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]