# Generated by Django 5.0 on 2024-03-04 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0019_rename_location_interview_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postjobs',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]
