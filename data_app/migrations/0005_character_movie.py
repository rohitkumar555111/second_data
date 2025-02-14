# Generated by Django 2.2.5 on 2020-05-07 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0004_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('movies', models.ManyToManyField(to='data_app.Movie')),
            ],
        ),
    ]
