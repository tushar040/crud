# Generated by Django 4.2.5 on 2023-10-17 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0024_studentform_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentform',
            name='mobile',
        ),
    ]
