# Generated by Django 5.1.2 on 2024-11-14 13:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_setting', '0002_setexam'),
        ('reports', '0007_alter_studentassessment_assessment_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentassessment',
            name='assessment_grade',
            field=models.ForeignKey(default='A', on_delete=django.db.models.deletion.CASCADE, to='exam_setting.gradescale'),
            preserve_default=False,
        ),
    ]
