# Generated by Django 5.0 on 2024-03-22 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0022_remove_resumescreening_seeker_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='status',
        ),
    ]
