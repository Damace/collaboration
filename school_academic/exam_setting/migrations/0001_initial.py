# Generated by Django 5.1.2 on 2024-10-25 00:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('mandatory', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='GradeDivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_name', models.CharField(max_length=255)),
                ('division_title', models.CharField(max_length=255)),
                ('minimum_division_point', models.FloatField()),
                ('sequence_order', models.PositiveIntegerField()),
                ('program_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_setting.programme')),
            ],
        ),
        migrations.CreateModel(
            name='GradeScale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_name', models.CharField(max_length=255)),
                ('minimum_marks', models.PositiveIntegerField()),
                ('grade_point', models.FloatField()),
                ('remark', models.TextField()),
                ('sequence_order', models.PositiveIntegerField()),
                ('program_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_setting.programme')),
            ],
        ),
    ]