# Generated by Django 4.2.5 on 2023-10-12 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0013_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='fname',
            new_name='f_name',
        ),
        migrations.RenameField(
            model_name='details',
            old_name='lname',
            new_name='l_name',
        ),
    ]