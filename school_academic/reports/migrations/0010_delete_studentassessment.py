# Generated by Django 5.1.2 on 2024-11-14 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_alter_studentassessment_assessment_grade'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentAssessment',
        ),
    ]