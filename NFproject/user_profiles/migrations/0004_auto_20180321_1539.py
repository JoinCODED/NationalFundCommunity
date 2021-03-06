# Generated by Django 2.0.2 on 2018-03-21 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0003_auto_20180308_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='individual',
            name='industry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_profiles.Industries'),
        ),
        migrations.AddField(
            model_name='organization',
            name='industry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_profiles.Industries'),
        ),
    ]
