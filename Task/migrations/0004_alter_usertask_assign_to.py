# Generated by Django 3.2.13 on 2022-07-16 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Task', '0003_rename_usertasks_usertask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='assign_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
