# Generated by Django 3.1.7 on 2021-03-29 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0009_auto_20210329_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
