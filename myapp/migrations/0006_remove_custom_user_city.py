# Generated by Django 5.1.2 on 2024-10-18 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_classschedule_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_user',
            name='city',
        ),
    ]