# Generated by Django 3.0.8 on 2020-09-11 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_customuser_solved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='solved',
        ),
    ]
