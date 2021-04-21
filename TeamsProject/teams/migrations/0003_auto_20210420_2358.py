# Generated by Django 3.2 on 2021-04-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20210420_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
