# Generated by Django 4.1.3 on 2022-11-21 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
    ]