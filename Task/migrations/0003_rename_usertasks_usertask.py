# Generated by Django 3.2.13 on 2022-07-16 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_rename_name_department_department_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserTasks',
            new_name='UserTask',
        ),
    ]
