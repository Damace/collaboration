# Generated by Django 5.1.2 on 2024-10-25 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_setting', '0005_subjectconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='status',
            field=models.CharField(choices=[('Core', 'Core'), ('Subsidiary', 'Subsidiary')], default='Core', max_length=10),
        ),
    ]