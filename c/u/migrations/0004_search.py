# Generated by Django 2.2.12 on 2023-04-06 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('u', '0003_worker_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]