# Generated by Django 2.2.12 on 2023-04-06 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('u', '0004_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
