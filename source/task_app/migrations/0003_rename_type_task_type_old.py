# Generated by Django 4.1 on 2022-10-11 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0002_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='type',
            new_name='type_old',
        ),
    ]
