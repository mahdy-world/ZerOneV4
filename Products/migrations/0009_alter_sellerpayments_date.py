# Generated by Django 3.2.5 on 2023-05-30 02:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0008_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 4, 51, 56, 44741), verbose_name='التاريخ'),
        ),
    ]
