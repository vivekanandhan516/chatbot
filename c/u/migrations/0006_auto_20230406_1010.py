# Generated by Django 2.2.12 on 2023-04-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('u', '0005_auto_20230406_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='userid',
            field=models.IntegerField(default=0),
        ),
    ]
