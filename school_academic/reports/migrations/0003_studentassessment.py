# Generated by Django 5.1.2 on 2024-11-11 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_annualreports_progressreports_subjectreports_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=20)),
                ('term', models.CharField(max_length=20)),
                ('programme', models.CharField(max_length=100)),
                ('student_class', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('assessment', models.CharField(max_length=100)),
                ('assessment_grade', models.CharField(max_length=2)),
            ],
        ),
    ]