# Generated by Django 2.2.5 on 2020-02-24 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='mobile',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
