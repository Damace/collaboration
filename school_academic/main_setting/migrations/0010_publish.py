# Generated by Django 5.1.2 on 2024-10-28 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_setting', '0009_resultsdeadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('publish', 'Publish'), ('unpublish', 'Unpublish')], default='unpublish', max_length=10)),
                ('program_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_setting.programme')),
            ],
        ),
    ]
