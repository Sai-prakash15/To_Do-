# Generated by Django 3.1.7 on 2021-03-23 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_todolist_modified_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='priority',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='modified_timestamp',
            field=models.DateTimeField(default=None),
        ),
    ]
