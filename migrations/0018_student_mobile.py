# Generated by Django 4.2.5 on 2023-10-13 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0017_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
