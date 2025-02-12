# Generated by Django 5.1.2 on 2024-11-21 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Record_results', '0021_alter_studentsassasmentsproxy_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsResultQue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=50)),
                ('entry_year', models.CharField(max_length=20)),
                ('entry_term', models.CharField(max_length=20)),
                ('entry_programme', models.CharField(max_length=100)),
                ('entry_class', models.CharField(max_length=50)),
                ('stream_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=100)),
                ('subject_code', models.CharField(max_length=100)),
                ('subject_name', models.CharField(max_length=100)),
                ('mt3', models.FloatField()),
                ('mt4', models.FloatField()),
                ('mte2', models.FloatField()),
                ('ae', models.FloatField()),
                ('hpbt1', models.FloatField()),
                ('hpbt2', models.FloatField()),
                ('hpbt3', models.FloatField()),
                ('average', models.FloatField()),
                ('grade', models.CharField(max_length=2)),
                ('remark', models.CharField(max_length=100)),
                ('position', models.IntegerField()),
            ],
        ),
    ]
