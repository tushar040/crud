# Generated by Django 4.2.5 on 2023-10-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0010_delete_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Action',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]