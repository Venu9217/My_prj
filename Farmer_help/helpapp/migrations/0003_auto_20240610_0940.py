# Generated by Django 3.0.5 on 2024-06-10 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpapp', '0002_auto_20240610_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop_db',
            name='land_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]