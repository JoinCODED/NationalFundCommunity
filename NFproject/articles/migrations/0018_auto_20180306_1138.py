# Generated by Django 2.0.2 on 2018-03-06 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_auto_20180306_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
