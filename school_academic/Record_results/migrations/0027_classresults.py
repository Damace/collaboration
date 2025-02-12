# Generated by Django 5.1.2 on 2024-11-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Record_results', '0026_studentsresult_result_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=50)),
                ('academic_year', models.CharField(max_length=50)),
                ('term', models.CharField(max_length=50)),
                ('subjects', models.TextField()),
                ('scores', models.TextField()),
            ],
        ),
    ]
