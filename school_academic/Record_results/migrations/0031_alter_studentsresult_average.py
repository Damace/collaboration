# Generated by Django 5.1.2 on 2024-11-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Record_results', '0030_classresults_entry_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsresult',
            name='average',
            field=models.FloatField(default=0.0),
        ),
    ]
