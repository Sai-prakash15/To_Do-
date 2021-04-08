# Generated by Django 3.1.7 on 2021-04-04 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0021_auto_20210404_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.TextField(blank=True, help_text='Enter field documentation', null=True)),
                ('modified_timestamp', models.DateTimeField(auto_now=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('1', 'Low'), ('2', 'Medium'), ('3', 'Important'), ('4', 'Critical')], max_length=1)),
                ('to_do_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskapp.todolist')),
            ],
        ),
    ]
