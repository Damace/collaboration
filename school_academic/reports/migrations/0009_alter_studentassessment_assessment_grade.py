# Generated by Django 5.1.2 on 2024-11-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_alter_studentassessment_assessment_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentassessment',
            name='assessment_grade',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
