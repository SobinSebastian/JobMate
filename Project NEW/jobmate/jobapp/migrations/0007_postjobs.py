# Generated by Django 4.2.7 on 2023-11-08 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_remove_job_providers_is_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostJobs',
            fields=[
                ('job_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Contract', 'Contract')], default='Full-Time', max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('minexp', models.CharField(default='Fresher', max_length=10)),
                ('pro_id', models.IntegerField(default=1)),
                ('status', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('salary', models.TextField(default='NOT DISCLOSED')),
                ('deadline', models.DateField(null=True)),
                ('mode', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline'), ('Both', 'Both')], default='Online', max_length=10)),
            ],
        ),
    ]
