# Generated by Django 3.2.5 on 2023-06-06 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Treasury', '0003_auto_20230606_0504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treasuryoperation',
            old_name='deleted',
            new_name='deleted_operation',
        ),
    ]
