# Generated by Django 4.2.5 on 2023-10-13 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0019_student_mobile1'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='color',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6),
        ),
    ]
