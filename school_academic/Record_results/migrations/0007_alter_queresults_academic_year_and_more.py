# Generated by Django 5.1.2 on 2024-11-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Record_results', '0006_alter_queresults_academic_year_alter_queresults_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queresults',
            name='academic_year',
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='queresults',
            name='class_name',
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='queresults',
            name='registration_number',
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='queresults',
            name='student_name',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='queresults',
            name='term',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]
