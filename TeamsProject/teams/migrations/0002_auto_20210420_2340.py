# Generated by Django 3.2 on 2021-04-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
