# Generated by Django 3.1.7 on 2021-04-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0013_auto_20210404_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='priority',
            field=models.IntegerField(blank=True),
        ),
    ]