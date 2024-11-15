# Generated by Django 5.1.2 on 2024-11-04 21:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_attendance', '0002_recordattendanceproxy'),
        ('main_setting', '0013_publish_published_by_publish_published_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline_date', models.DateField()),
                ('remark', models.TextField(blank=True, null=True)),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='main_setting.subject')),
            ],
        ),
    ]
