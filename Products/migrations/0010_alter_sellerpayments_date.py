# Generated by Django 3.2.5 on 2023-05-30 02:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 4, 53, 31, 806378), verbose_name='التاريخ'),
        ),
    ]