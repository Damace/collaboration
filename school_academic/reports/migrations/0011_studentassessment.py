# Generated by Django 5.1.2 on 2024-11-14 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_setting', '0002_setexam'),
        ('reports', '0010_delete_studentassessment'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(blank=True, max_length=20, null=True)),
                ('term', models.CharField(blank=True, max_length=20, null=True)),
                ('programme', models.CharField(blank=True, max_length=100, null=True)),
                ('student_class', models.CharField(blank=True, max_length=50, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('assessment', models.CharField(blank=True, max_length=100, null=True)),
                ('assessment_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_setting.gradescale')),
            ],
        ),
    ]